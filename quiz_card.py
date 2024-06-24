# Card class
# Stores information for each card.
# As a study aid, each card carries a key point and key info regarding that point
# Key points could be a statement, term, question, etc. and key info could be additional info, definition, answer, etc.

class QuizCard:
    # Called on object instantiation
    def __init__(self, id, chapter, objective, section, frontside, backside, needs_review):
        self.id = id
        self.chapter = chapter
        self.objective = objective
        self.section = section
        self.frontside = frontside
        self.backside = backside
        self.needs_review = needs_review
