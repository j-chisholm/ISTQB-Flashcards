# UI Manager class
# Handles updating the UI

import sys

from deck import Deck
from quiz_card import QuizCard
from file_manager import FileManager


from PyQt6 import QtWidgets
from pyqt_ui import Ui_MainWindow

class AppManager():

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.LoadTheme()
        self.MainWindow.setWindowTitle("ISTQB CTFL Flash Cards")
        self.MainWindow.show()

        self.deck = Deck()

        self.current_card_index = 0
        self.is_card_detail_visible = True

        self.LoadCards()
        self.UpdateUIElements()
        self.UpdateActiveDeck()

        self.ConnectSignals()

        sys.exit((self.app.exec()))

    # method to modify the theme
    def LoadTheme(self):
        # load the dark theme
        stylesheet = """
        QWidget {
          background-color: #333333;
          color: #ffffff;
        }
        """

        # Apply the stylesheet to the main window
        self.MainWindow.setStyleSheet(stylesheet)


    # connect button signals to the appropriate method calls
    def ConnectSignals(self):
        self.ui.next_card_btn.clicked.connect(self.NextCard)
        self.ui.prev_card_btn.clicked.connect(self.PreviousCard)
        self.ui.show_details_btn.clicked.connect(self.DisplayCurrentCardDetails)
        self.ui.chapter_combobox.currentTextChanged.connect(self.UpdateActiveDeck)
        self.ui.objective_combobox.currentTextChanged.connect(self.UpdateActiveDeck)
        self.ui.section_combobox.currentTextChanged.connect(self.UpdateActiveDeck)
        self.ui.needs_review_filter.clicked.connect(self.UpdateActiveDeck)
        self.ui.refresh_btn.clicked.connect(self.UpdateActiveDeck)
        self.ui.mark_review_btn.clicked.connect(self.ToggleMarkForReview)
        self.ui.reset_filters_btn.clicked.connect(self.ClearFilters)
        self.ui.show_review_cards_btn.clicked.connect(lambda: self.ClearFilters(True))

    def LoadCards(self):
        # file path
        FILE_NAME = "testJSON.json"

        # create a file manager
        file_manager = FileManager()
        card_data = file_manager.ParseJSON(FILE_NAME)

        # store all cards in the deck and assign index
        id = 0
        for data in card_data:
            self.deck.active_cards.append((QuizCard(
                id,
                data["chapter"],
                data["objective"],
                data["section"],
                data["key_point"],
                data["key_info"],
                data["needs_review"]
            )))

            id += 1

    # update the Active deck with user's filters
    def UpdateActiveDeck(self):
        self.deck.chapter_filter = int(self.ui.chapter_combobox.currentText())
        self.deck.objective_filter = int(self.ui.objective_combobox.currentText())
        self.deck.section_filter = int(self.ui.section_combobox.currentText())
        self.deck.review_filter = self.ui.needs_review_filter.isChecked()
        self.deck.FilterDeck()

        self.current_card_index = 0
        self.UpdateUIElements()
        self.DisplayCurrentCardKeyPoint()

    # resets all filters to default values
    def ClearFilters(self, show_checked=False):
        self.ui.chapter_combobox.setCurrentText("0")
        self.ui.objective_combobox.setCurrentText("0")
        self.ui.section_combobox.setCurrentText("0")
        self.ui.needs_review_filter.setChecked(show_checked)

        self.UpdateActiveDeck()

    # displays the key point section of the current card
    def DisplayCurrentCardKeyPoint(self):
        if self.deck.active_cards:
            current_card = self.deck.active_cards[self.current_card_index]
            self.ui.key_points_textbox.setText(current_card.key_point)
            self.UpdateUIElements()
        else:
            self.ui.key_points_textbox.setText("No cards matching those filters...")
            self.ResetUIElements()

        self.ui.details_textbox.clear()

    # display the details section for the current card
    def DisplayCurrentCardDetails(self):
        if self.deck.active_cards:
            current_card = self.deck.active_cards[self.current_card_index]
            self.ui.details_textbox.setText(current_card.key_info)
            #update the show details button
            if self.ui.show_details_btn.text() == "Show Details":
                self.ui.show_details_btn.setText("Hide Details")
            else:
                self.ui.show_details_btn.setText("Show Details")
                self.ui.details_textbox.clear()
            self.UpdateUIElements()
        else:
            self.ui.details_textbox.setText("No cards matching those filters...")
            self.ResetUIElements()


    # retrieves the next card in the active deck
    def NextCard(self):
        if self.deck.active_cards:
            self.current_card_index = (self.current_card_index + 1) % len(self.deck.active_cards)
        self.DisplayCurrentCardKeyPoint()

    # retrieves the previous card in the active deck
    def PreviousCard(self):
        if self.deck.active_cards:
            self.current_card_index = (self.current_card_index - 1) % len(self.deck.active_cards)
        self.DisplayCurrentCardKeyPoint()

    # updates the dynamic ui elements
    def UpdateUIElements(self):
        # update the card progress tracker (current # in the deck vs total # number in the deck)
        self.ui.card_progress_label.setText(f"CARD {self.current_card_index + 1}/{len(self.deck.active_cards)}")

        if self.deck.active_cards:
            # update the marked for review label
            if self.deck.active_cards[self.current_card_index].needs_review:
                self.ui.review_label.setStyleSheet("color: red;")
                self.ui.mark_review_btn.setText("Clear Review Mark")
            else:
                self.ui.review_label.setStyleSheet("color:rgba(255, 255, 255, 0)")
                self.ui.mark_review_btn.setText("Mark For Review")

    # reset the ui elements to their default state
    def ResetUIElements(self):
        # reset the card progress tracker
        self.ui.card_progress_label.setText(f"CARD 0/0")
        #reset the marked for review label
        self.ui.review_label.setStyleSheet("color:rgba(255, 255, 255, 0)")

    # marks the card for review if it is not marked and unmarks it if it is marked.
    def ToggleMarkForReview(self):
        self.deck.active_cards[self.current_card_index].needs_review =\
            not self.deck.active_cards[self.current_card_index].needs_review

        self.UpdateUIElements()
