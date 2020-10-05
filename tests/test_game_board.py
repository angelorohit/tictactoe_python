import unittest
from game.game_board import GameBoard
from game.player import Player
from utilities import input_cases


class TestGameBoard(unittest.TestCase):
    def test_init(self):
        game_board = GameBoard(Player('Player1', 'X'),
                               Player('Player2', 'O'), size=3)
        self.assertEqual(game_board.size, 3)
        self.assertEqual(game_board.grid, ([None, None, None],
                                           [None, None, None],
                                           [None, None, None]))

    def test_clear(self):
        game_board = GameBoard(Player('Player1', 'X'),
                               Player('Player2', 'O'), size=3)
        game_board.clear(size=4)
        self.assertEqual(game_board.size, 4)
        self.assertTupleEqual(game_board.grid, ([None, None, None, None],
                                                [None, None, None, None],
                                                [None, None, None, None],
                                                [None, None, None, None]))

    @input_cases({
        '4': 4,
        '9': 9,
        '-1': 3,
        'abc': 3,
        '2': 3,
        '10': 3,
        ' ': 3})
    def test_gather_board_size(self, expected_size):
        game_board = GameBoard(Player('Player1', 'X'),
                               Player('Player2', 'O'), size=3)
        game_board.gather_board_size()
        self.assertEqual(game_board.size, expected_size)
        self.assertTupleEqual(game_board.grid, tuple([None for pos in range(0, expected_size)]
                                                     for row in range(0, expected_size)))


if __name__ == '__main__':
    unittest.main()
