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
        self.MainWindow.show()

        self.complete_deck = None
        self.study_deck = []

        self.current_card_index = 0
        self.is_card_detail_visible = True

        self.LoadCards()
        self.UpdateCardProgress()
        self.UpdateStudyDeck()

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


    def ConnectSignals(self):
        # connect the next card button to the NextCard method
        self.ui.next_card_btn.clicked.connect(self.NextCard)
        # connect the prev card button to the PreviousCard method
        self.ui.prev_card_btn.clicked.connect(self.PreviousCard)
        # connect the flip card button to the FlipCard method
        self.ui.show_details_btn.clicked.connect(self.DisplayCurrentCardDetails)
        # connect the chapter spin button to UpdateStudyDeck method
        self.ui.chapter_spin_box.valueChanged.connect(self.UpdateStudyDeck)
        # connect the objective spin button to UpdateStudyDeck method
        self.ui.objective_spin_box.valueChanged.connect(self.UpdateStudyDeck)
        # connect the section spin button to UpdateStudyDeck method
        self.ui.section_spin_box.valueChanged.connect(self.UpdateStudyDeck)

    def LoadCards(self):
        # file path
        FILE_NAME = "testJSON.json"

        # create a file manager
        file_manager = FileManager()
        card_data = file_manager.ParseJSON(FILE_NAME)

        self.complete_deck = Deck()

        # store all cards in n complete deck
        for data in card_data:
            self.complete_deck.AddCard(QuizCard(
                data["chapter"],
                data["objective"],
                data["section"],
                data["key_point"],
                data["key_info"]
            ))

        # set study deck to all cards in the complete deck
        self.study_deck = self.complete_deck.cards

    # update the study deck with user's filters
    def UpdateStudyDeck(self):
        self.complete_deck.chapter_filter = self.ui.chapter_spin_box.value()
        self.complete_deck.objective_filter = self.ui.objective_spin_box.value()
        self.complete_deck.section_filter = self.ui.section_spin_box.value()
        self.study_deck = self.complete_deck.FilterDeck()

        self.current_card_index = 0
        self.UpdateCardProgress()
        self.DisplayCurrentCardKeyPoint()

    # displays the key point section of the current card
    def DisplayCurrentCardKeyPoint(self):
        if self.study_deck:
            current_card = self.study_deck[self.current_card_index]
            self.ui.key_points_textbox.setText(current_card.key_point)
        else:
            self.ui.key_points_textbox.setText("No cards matching those filters...")

        self.UpdateCardProgress()
        self.ui.details_textbox.clear()

    # display the details section for the current card
    def DisplayCurrentCardDetails(self):
        if self.study_deck:
            current_card = self.study_deck[self.current_card_index]
            self.ui.details_textbox.setText(current_card.key_info)
        else:
            self.ui.details_textbox.setText("No cards matching those filters...")

        self.UpdateCardProgress()

    # retrieves the next card in the study_deck
    def NextCard(self):
        if self.study_deck:
            self.current_card_index = (self.current_card_index + 1) % len(self.study_deck)
        self.DisplayCurrentCardKeyPoint()


    # retrieves the previous card in the study_deck
    def PreviousCard(self):
        if self.study_deck:
            self.current_card_index = (self.current_card_index - 1) % len(self.study_deck)
        self.DisplayCurrentCardKeyPoint()

    def UpdateCardProgress(self):
        self.ui.card_progress_label.setText(f"CARD {self.current_card_index + 1}/{len(self.study_deck)}")

    # method to aid with debugging
    def DebugDisplayCards(self):
        for card in self.study_deck:
            card.DebugReadInfo()

app_manager = AppManager()
