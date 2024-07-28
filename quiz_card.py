# Card class
# Stores information for each card.
# As a study aid, each card carries a key point and key info regarding that point
# Key points could be a statement, term, question, etc. and key info could be additional info, definition, answer, etc.

class QuizCard:
    # Called on object instantiation
    def __init__(self, id, chapter, objective, section, frontside, backside, needs_review):
        self.id = id
        self.chapter = str(chapter)
        self.objective = str(objective)
        self.section = str(section)
        self.frontside = frontside
        self.backside = backside
        self.needs_review = needs_review

    # define how each card is compared to another using "<" for the list.sort() method
    def __lt__(self, other):
        self.chapter = self.chapter
        if self.chapter < other.chapter:
            return True
        elif self.chapter == other.chapter:
            if self.objective < other.objective:
                return True
            elif self.objective == other.objective:
                if self.section <= other.section:
                    return True
        else:
            return False
