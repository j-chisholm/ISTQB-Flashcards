# Deck class
# Stores a list of quiz cards and their quiz related information (card front, card back)

class Deck:
    # Called on object instantiation
    def __init__(self):
        self.active_cards = []
        self.inactive_cards = []
        self.chapter_filter = 0
        self.objective_filter = 0
        self.section_filter = 0
        self.review_filter = False

    def FilterDeck(self):
        deactivate_cards = []
        # search active_cards for cards that do not meet the filter conditions
        for card in self.active_cards:
            if not ((self.chapter_filter == 0 or card.chapter == self.chapter_filter) and
                    (self.objective_filter == 0 or card.objective == self.objective_filter) and
                    (self.section_filter == 0 or card.section == self.section_filter) and
                    (card.needs_review == self.review_filter)):
                # add card to the list to deactivate
                deactivate_cards.append(card)

        activate_cards = []
        # search inactive_cards for cards that meet the filter conditions
        for card in self.inactive_cards:
            if (self.chapter_filter == 0 or card.chapter == self.chapter_filter) and \
                    (self.objective_filter == 0 or card.objective == self.objective_filter) and \
                    (self.section_filter == 0 or card.section == self.section_filter) and \
                    (card.needs_review == self.review_filter):
                # add card to the list to activate
                activate_cards.append(card)

        # move cards to the appropriate list
        for card in deactivate_cards:
            self.active_cards.remove(card)
            self.inactive_cards.append(card)

        for card in activate_cards:
            self.active_cards.append(card)
            self.inactive_cards.remove(card)
