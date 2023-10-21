"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    def __init__(self, path):
        dictionary = open(path)
        self.words = self.parse(dictionary)
        print(f"{len(self.words)} words read")

    def parse(self, dictionary):
        """Parse dictionary -> list of words."""

        return [w.strip() for w in dictionary]  

    def random(self):
        """returns radom word"""

        return random.choice(self.words)  

class SpecialWordFinder(WordFinder):
    def parse(self, dictionary):
        """Parse dictionary -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dictionary
                if w.strip() and not w.startswith("#")]
