import unittest
from game.player import Player
from utilities import input_cases


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player = Player('Random name', 'X')
        self.assertEqual(player.name, 'Random name')
        self.assertEqual(player.symbol, 'X')

    @input_cases({
        # Valid new name should update the player's name to the new one
        'New name': 'New name',
        # Empty name should not update the player's name
        ' ': 'Original name'})
    def test_gather_input(self, expected_name):
        player = Player('Original name', 'X')
        player.gather_name()
        self.assertEqual(player.name, expected_name)

    @input_cases({
        # Lower case input
        'a1': (0, 0, None),
        # Upper case input
        'C3': (2, 2, None),
        # Input too long
        'a12': (0, 0, 'You must enter a position as the letter column and number row. Example, A1 or C2'),
        # Column input is not a letter
        '-1': (0, 0, 'You must enter a position as the letter column and number row. Example, A1 or C2'),
        # Row is not a digit
        'C-': (0, 0, 'You must enter a position as the letter column and number row. Example, A1 or C2'),
        # Row exceeds game board size
        'C4': (0, 0, 'You must enter a row value that is within the playing board size of 1 to 3'),
        # Column exceeds game board size
        'D1': (0, 0, 'You must enter a column value that is within the playing board size of A to C')})
    def test_take_turn(self, expected_output):
        player = Player('Alice', 'X')
        turn_result = player.take_turn(game_board_size=3)
        self.assertEqual(turn_result, expected_output)


if __name__ == '__main__':
    unittest.main()
