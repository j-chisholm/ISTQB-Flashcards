# Card class
# Stores information for each card.
# As a study aid, each card carries a key point and key info regarding that point
# Key points could be a statement, term, question, etc. and key info could be additional info, definition, answer, etc.

class QuizCard:
    # Called on object instantiation
    def __init__(self, chapter, objective, section, key_point, key_info):
        self.chapter = chapter
        self.objective = objective
        self.section = section
        self.key_point = key_point
        self.key_info = key_info

    # Displays the key topic of the card
    def ShowKeyPoint(self):
        print(self.key_point)

    # Displays the key info of the card
    def ShowKeyInfo(self):
        print(self.key_info)

    def DebugReadInfo(self):
        print(self.chapter)
        print(self.objective)
        print(self.section)
        print(self.key_point)
        print(self.key_info)
