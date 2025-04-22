import string
from random import choice

class Game:
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = [choice(string.ascii_uppercase) for i in range(9)]


    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""

        if len(word) == 0:
            return False
        for letter in word:
            if letter in set(self.grid):
                continue
            else:
                return False
        return True
