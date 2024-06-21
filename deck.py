# Deck class
# Stores a list of quiz cards and their quiz related information (key_point, key_information)

class Deck:
    # Called on object instantiation
    def __init__(self):
        self.cards = []

    def AddCard(self, card):
        self.cards.append(card)

    def FilterDeck(self, chapter, objective, section):
        study_deck = []
        for card in self.cards:
            if (chapter is None or card.chapter == chapter) and \
                    (objective is None or card.objective == objective) and \
                    (section is None or card.section == section):
                study_deck.append(card)

        return study_deck
