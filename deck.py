# Deck class
# Stores a list of quiz cards and their quiz related information (card front, card back)

import random

class Deck:
    # Called on object instantiation
    def __init__(self):
        self.active_cards = []
        self.inactive_cards = []
        self.chapter_filter = 0
        self.objective_filter = 0
        self.section_filter = 0
        self.hide_review_cards_on_update = False

    def FilterDeck(self):
        deactivate_cards = []
        # search active_cards for cards that do not meet the filter conditions
        for card in self.active_cards:
            if not ((self.chapter_filter == 0 or card.chapter == self.chapter_filter) and
                    (self.objective_filter == 0 or card.objective == self.objective_filter) and
                    (self.section_filter == 0 or card.section == self.section_filter)):
                # add card to the list to deactivate
                deactivate_cards.append(card)
            else:  # card meets filter conditions
                # filter out review cards based on user preference
                if self.hide_review_cards_on_update:
                    if card.needs_review:
                        deactivate_cards.append(card)

        activate_cards = []
        # search inactive_cards for cards that meet the filter conditions
        for card in self.inactive_cards:
            if ((self.chapter_filter == 0 or card.chapter == self.chapter_filter) and
                    (self.objective_filter == 0 or card.objective == self.objective_filter) and
                    (self.section_filter == 0 or card.section == self.section_filter)):

                # filter out review cards based on user preference
                if self.hide_review_cards_on_update:
                    if card.needs_review:
                        deactivate_cards.append(card)
                else:
                    # add card to the list to activate
                    activate_cards.append(card)

        # move cards to the appropriate list
        for card in deactivate_cards:
            self.active_cards.remove(card)
            self.inactive_cards.append(card)

        for card in activate_cards:
            self.active_cards.append(card)
            self.inactive_cards.remove(card)

    # filter the deck to show only cards under review
    def FilterOnlyReviewCards(self):
        deactivate_cards = []
        # set cards to deactivate
        for card in self.active_cards:
            if not card.needs_review:
                deactivate_cards.append(card)

        activate_cards = []
        # set cards to activate
        for card in self.inactive_cards:
            if card.needs_review:
                activate_cards.append(card)

        # move cards to the appropriate list
        for card in deactivate_cards:
            self.active_cards.remove(card)
            self.inactive_cards.append(card)

        for card in activate_cards:
            self.active_cards.append(card)
            self.inactive_cards.remove(card)

    # randomizes the order of cards in the deck
    def ShuffleDeck(self):
        random.shuffle(self.active_cards)

    # order the cards in ascending or descending order
    def OrderDeck(self, rev=False):
        deck = self.active_cards + self.inactive_cards

        # sort the cards
        # updating only active cards would require the user to order the cards after each time they filter the deck
        deck.sort(reverse=rev)
        self.active_cards = deck
        self.inactive_cards = []

