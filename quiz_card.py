# Card class
# Stores information for each card.
# As a study aid, each card carries a key point and key info regarding that point
# Key points could be a statement, term, question, etc. and key info could be additional info, definition, answer, etc.

class QuizCard:
    # Called on object instantiation
    def __init__(self, id, chapter, objective, section, key_point, key_info, needs_review):
        self.id = id
        self.chapter = chapter
        self.objective = objective
        self.section = section
        self.key_point = key_point
        self.key_info = key_info
        self.needs_review = needs_review

    # Displays the key topic of the card
    def ShowKeyPoint(self):
        print(self.key_point)

    # Displays the key info of the card
    def ShowKeyInfo(self):
        print(self.key_info)
