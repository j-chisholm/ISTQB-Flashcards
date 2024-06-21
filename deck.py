# Deck class
# Stores a list of quiz cards and their quiz related information (key_point, key_information)

class Deck:
    # Called on object instantiation
    def __init__(self):
        self.cards = []
        self.chapter_filter = 0
        self.objective_filter = 0
        self.section_filter = 0

    def AddCard(self, card):
        self.cards.append(card)

    def FilterDeck(self):
        study_deck = []
        for card in self.cards:
            if (self.chapter_filter == 0 or card.chapter == self.chapter_filter) and \
                    (self.objective_filter == 0 or card.objective == self.objective_filter) and \
                    (self.section_filter == 0 or card.section == self.section_filter):
                study_deck.append(card)

        return study_deck
