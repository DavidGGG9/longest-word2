from longest_word2.game import Game
import sys
import string

class TestGame:
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid

        assert isinstance(grid, list)
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

    def test_empty_word_is_invalid(self):
        new_game = Game()
        grid = new_game.grid

        player_input = ''

        assert new_game.is_valid(player_input) == False

    def test_word_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KJZENRIAZ')
        player_input = 'SANDWICH'

        assert new_game.is_valid(player_input) == False

    def test_word_is_valid(self):
        new_game = Game()
        new_game.grid = list('YRAPENVTO')
        player_input = 'ENTROPY'

        assert new_game.is_valid(player_input) == True
