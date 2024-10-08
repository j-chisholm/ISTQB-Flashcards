# UI Manager class
# Handles updating the UI
import sys

from deck import Deck
from file_manager import FileManager

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog
from pyqt_ui import Ui_MainWindow

class AppManager:

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.LoadStylesheet()
        self.MainWindow.setWindowTitle("ISTQB CTFL Flash Cards")
        self.MainWindow.show()

        self.file_manager = FileManager()
        self.deck = Deck()

        self.current_card_index = 0
        self.is_card_detail_visible = True
        self.show_only_review_cards = False

        self.OpenCardsFile()

        self.UpdateUIElements()
        self.UpdateActiveDeck()

        self.ConnectSignals()

        sys.exit((self.app.exec()))

    # method to modify the theme
    def LoadStylesheet(self):
        # load the stylesheet
        file = open("styles.qss", "r")
        stylesheet = file.read()
        file.close()

        # Apply the stylesheet to the main window
        self.MainWindow.setStyleSheet(stylesheet)

    # connect signals to the appropriate method calls
    def ConnectSignals(self):
        self.ui.next_card_btn.clicked.connect(self.NextCard)
        self.ui.prev_card_btn.clicked.connect(self.PreviousCard)
        self.ui.show_details_btn.clicked.connect(self.DisplayCurrentCardBackside)
        self.ui.chapter_combobox.currentTextChanged.connect(self.UpdateActiveDeck)
        self.ui.objective_combobox.currentTextChanged.connect(self.UpdateActiveDeck)
        self.ui.section_combobox.currentTextChanged.connect(self.UpdateActiveDeck)
        self.ui.refresh_btn.clicked.connect(self.UpdateActiveDeck)
        self.ui.mark_review_btn.clicked.connect(self.ToggleMarkForReview)
        self.ui.reset_filters_btn.clicked.connect(self.ClearFilters)
        self.ui.show_review_cards_btn.clicked.connect(self.ShowCardsUnderReview)
        self.ui.actionSave_Cards.triggered.connect(self.SaveCardsToFile)
        self.ui.actionOpen_Cards.triggered.connect(self.OpenCardsFile)
        self.ui.prefHide_Marked_For_Review.triggered.connect(self.ReviewMarkPreference)
        self.ui.actionShuffle_Cards.triggered.connect(self.ShuffleDeck)
        self.ui.actionAscending.triggered.connect(self.OrderDeck)
        self.ui.actionDescending.triggered.connect(lambda: self.OrderDeck(rev=True))

    # update the Active deck with user's filters
    def UpdateActiveDeck(self):
        self.deck.chapter_filter = self.ui.chapter_combobox.currentText()
        self.deck.objective_filter = self.ui.objective_combobox.currentText()
        self.deck.section_filter = self.ui.section_combobox.currentText()
        self.deck.hide_review_cards_on_update = self.ui.prefHide_Marked_For_Review.isChecked()

        self.deck.FilterDeck()

        self.current_card_index = 0
        self.DisplayCurrentCardFrontside()

    # resets all filters to default values
    def ClearFilters(self):
        self.ui.chapter_combobox.setCurrentText("Any")
        self.ui.objective_combobox.setCurrentText("Any")
        self.ui.section_combobox.setCurrentText("Any")

        self.UpdateActiveDeck()

    # displays the front of the current card
    def DisplayCurrentCardFrontside(self):
        if self.deck.active_cards:
            current_card = self.deck.active_cards[self.current_card_index]
            self.ui.card_front_textbox.setText(current_card.frontside)
            self.UpdateUIElements()

            # set the Show/Hide Details button to default state
            self.ui.show_details_btn.setText("Show Details")

        else:
            self.ui.card_front_textbox.setText("No cards matching those filters...")
            self.ResetUIElements()

        self.ui.card_back_textbox.clear()

    # display the details section for the current card
    def DisplayCurrentCardBackside(self):
        if self.deck.active_cards:
            current_card = self.deck.active_cards[self.current_card_index]
            self.ui.card_back_textbox.setText(current_card.backside)
            # update the show details button
            if self.ui.show_details_btn.text() == "Show Details":
                self.ui.show_details_btn.setText("Hide Details")
            else:
                self.ui.show_details_btn.setText("Show Details")
                self.ui.card_back_textbox.clear()
            self.UpdateUIElements()
        else:
            self.ResetUIElements()

    # retrieves the next card in the active deck
    def NextCard(self):
        if self.deck.active_cards:
            self.current_card_index = (self.current_card_index + 1) % len(self.deck.active_cards)
        self.DisplayCurrentCardFrontside()
        self.ui.show_details_btn.setText("Show Details")

    # retrieves the previous card in the active deck
    def PreviousCard(self):
        if self.deck.active_cards:
            self.current_card_index = (self.current_card_index - 1) % len(self.deck.active_cards)
        self.DisplayCurrentCardFrontside()
        self.ui.show_details_btn.setText("Show Details")

    # updates the dynamic ui elements
    def UpdateUIElements(self):
        if self.deck.active_cards:
            # update the card progress tracker (current # in the deck vs total # number in the deck)
            self.ui.card_progress_label.setText(f"CARD {self.current_card_index + 1}/{len(self.deck.active_cards)}")
            # update the marked for review label
            if self.deck.active_cards[self.current_card_index].needs_review:
                self.ui.review_label.setStyleSheet("color: #8a63d2;")
                self.ui.mark_review_btn.setText("Clear Review Mark")
            else:
                self.ui.review_label.setStyleSheet("color:rgba(255, 255, 255, 0)")
                self.ui.mark_review_btn.setText("Mark For Review")

    # reset the ui elements to their default state
    def ResetUIElements(self):
        # reset the card progress tracker
        self.ui.card_progress_label.setText(f"CARD 0/0")
        # reset the marked for review label
        self.ui.review_label.setStyleSheet("color:rgba(255, 255, 255, 0)")

    # marks the card for review if it is not marked and unmarks it if it is marked.
    def ToggleMarkForReview(self):
        if self.deck.active_cards:
            self.deck.active_cards[self.current_card_index].needs_review =\
                not self.deck.active_cards[self.current_card_index].needs_review

        self.UpdateUIElements()

    # save the current deck to a file
    def SaveCardsToFile(self):
        # open a file dialog to select the save file
        file_name, _ = QFileDialog.getSaveFileName(self.MainWindow, "Save File", "", "JSON Files (*.json)")
        if file_name:
            self.file_manager.SaveDeckToFile(self.deck, file_name)

    # opens a card file (json format)
    def OpenCardsFile(self):
        # open a file dialog to select a file
        file_name, _ = QFileDialog.getOpenFileName(self.MainWindow, "Open File", "", "JSON Files (*.json)")
        if file_name:
            # reset the deck
            self.deck.active_cards = []
            self.deck.inactive_cards = []
            # load deck from file
            self.file_manager.LoadDeckFromFile(self.deck, file_name)
            self.file_manager.last_open_file = file_name
            # update the ui
            self.UpdateActiveDeck()
            self.UpdateUIElements()

    # set the user's preference for displaying cards marked for review
    def ReviewMarkPreference(self):
        if self.ui.prefHide_Marked_For_Review.isChecked():
            self.deck.hide_review_cards_on_update = True
        else:
            self.deck.hide_review_cards_on_update = False

        self.UpdateActiveDeck()

    # show only the cards under review
    def ShowCardsUnderReview(self):
        self.ClearFilters()
        self.ui.prefHide_Marked_For_Review.setChecked(False)
        self.deck.FilterOnlyReviewCards()
        self.UpdateUIElements()

    # shuffle the deck
    def ShuffleDeck(self):
        self.deck.ShuffleDeck()
        self.UpdateActiveDeck()

    # order the cards
    def OrderDeck(self, rev=False):
        self.deck.OrderDeck(rev=rev)
        self.deck.FilterDeck()
        self.UpdateActiveDeck()
