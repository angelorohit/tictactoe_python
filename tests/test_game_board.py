import unittest

import numpy as np
from game.game_board import GameBoard
from game.player import Player

from utilities import input_cases


class TestGameBoard(unittest.TestCase):
    def test_init(self):
        game_board = GameBoard(size=3)
        self.assertEqual(game_board.size, 3)
        self.assertTupleEqual(np.shape(game_board.grid), (3, 3))
        self.assertTrue(np.all(game_board.grid == None))

    def test_clear(self):
        game_board = GameBoard(size=3)
        game_board.clear(size=4)
        self.assertEqual(game_board.size, 4)
        self.assertTupleEqual(np.shape(game_board.grid), (4, 4))
        self.assertTrue(np.all(game_board.grid == None))

    @input_cases({
        '4': 4,
        '9': 9,
        '-1': 3,
        'abc': 3,
        '2': 3,
        '10': 3,
        ' ': 3})
    def test_gather_board_size(self, expected_size):
        game_board = GameBoard(size=3)
        game_board.gather_board_size()
        self.assertEqual(game_board.size, expected_size)
        self.assertTupleEqual(np.shape(game_board.grid),
                              (expected_size, expected_size))
        self.assertTrue(np.all(game_board.grid == None))

    def test_render(self):
        game_board = GameBoard(size=3)
        render_result = game_board.render()
        self.assertEqual(render_result,
                         "    A   B   C   \n"
                         "1 | - | - | - | \n"
                         "2 | - | - | - | \n"
                         "3 | - | - | - | \n")
        game_board.make_player_move(0, 0, Player('Player1', 'X'))
        render_result = game_board.render()
        self.assertEqual(render_result,
                         "    A   B   C   \n"
                         "1 | X | - | - | \n"
                         "2 | - | - | - | \n"
                         "3 | - | - | - | \n")
        game_board.make_player_move(1, 1, Player('Player2', 'O'))
        render_result = game_board.render()
        self.assertEqual(render_result,
                         "    A   B   C   \n"
                         "1 | X | - | - | \n"
                         "2 | - | O | - | \n"
                         "3 | - | - | - | \n")

    def test_make_player_move(self):
        player1 = Player('Player1', 'X')
        player2 = Player('Player2', 'O')
        game_board = GameBoard(size=3)
        existing_player = game_board.make_player_move(0, 0, player1)
        self.assertIsNone(existing_player)
        existing_player = game_board.make_player_move(0, 0, player2)
        self.assertEqual(existing_player, player1)
        existing_player = game_board.make_player_move(1, 1, player2)
        self.assertIsNone(existing_player)
        existing_player = game_board.make_player_move(1, 1, player1)
        self.assertEqual(existing_player, player2)


if __name__ == '__main__':
    unittest.main()
