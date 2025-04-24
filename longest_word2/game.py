import string
from random import choice
import requests

class Game:
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = [choice(string.ascii_uppercase) for i in range(9)]


    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""

        if len(word) == 0:
            return False
        for letter in word:
            if letter not in set(self.grid):
                return False

        URL = f'https://dictionary.lewagon.com/{word.lower()}'
        response = requests.get(URL)

        if response.status_code != 200 or response.json()['found'] is False:
            return False

        return True
