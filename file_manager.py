# Parser class
# Parses the given JSON file

import json

from quiz_card import QuizCard

class FileManager:
    # Called on object instantiation
    def __init__(self):
        self.last_open_file = ""

    # Save all cards to a file
    def SaveDeckToFile(self, deck, file_name):
        # open file for writing (overwrites the file)
        file = open(file_name, "w")

        card_list = []
        # build a dictionary for each card in active cards
        for card in deck.active_cards:
            card_dict = {
                "chapter": card.chapter,
                "objective": card.objective,
                "section": card.section,
                "frontside": card.frontside,
                "backside": card.backside,
                "needs_review": card.needs_review
            }
            card_list.append(card_dict)

        # build a dictionary for each card in inactive cards
        for card in deck.inactive_cards:
            card_dict = {
                "chapter": card.chapter,
                "objective": card.objective,
                "section": card.section,
                "frontside": card.frontside,
                "backside": card.backside,
                "needs_review": card.needs_review
            }
            card_list.append(card_dict)

        # convert the card_dict to json and write the card to the file
        file.write(json.dumps(card_list, separators=(',', ':'), indent=1))

        file.close()

    # Load all cards from a file
    def LoadDeckFromFile(self, deck, file_name):
        # read file contents
        try:
            with open(file_name, 'r') as json_file:
                pure_json = json_file.read()
            json_file.close()

            card_data = json.loads(pure_json)

            self.last_open_file = file_name
        except FileNotFoundError:
            return 0
        except json.decoder.JSONDecodeError:
            return 0

        # store all cards in the deck and assign index
        id = 0
        for data in card_data:
            deck.active_cards.append((QuizCard(
                id,
                data["chapter"],
                data["objective"],
                data["section"],
                data["frontside"],
                data["backside"],
                data["needs_review"]
            )))
            id += 1

        return 1

