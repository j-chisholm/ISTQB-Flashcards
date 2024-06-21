from file_manager import FileManager
from deck import Deck
from quiz_card import QuizCard

# file path
FILE_NAME = "C:\\Users\\jevon\\Projects\\ISTQB Flashcards\\testJSON.json"

# create a file manager
file_manager = FileManager()
card_data = file_manager.parse_json(FILE_NAME)

complete_deck = Deck()

# store all cards in n complete deck
for data in card_data:
    complete_deck.AddCard(QuizCard(
        data["chapter"],
        data["objective"],
        data["section"],
        data["key_point"],
        data["key_info"]
    ))

chapter = None
objective = None
section = None

study_deck = complete_deck.FilterDeck(chapter, objective, section)
for card in study_deck:
    card.DebugReadInfo()
    print()
