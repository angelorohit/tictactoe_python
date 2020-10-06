import unittest

import numpy as np
from game.game_board import GameBoard
from game.player import Player

from utilities import input_cases


class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.game_board = GameBoard(size=3)

    def test_init(self):
        self.assertEqual(self.game_board.size, 3)
        self.assertTupleEqual(np.shape(self.game_board.grid), (3, 3))
        self.assertTrue(np.all(self.game_board.grid == None))

    def test_clear(self):
        self.game_board.clear(size=4)

        self.assertEqual(self.game_board.size, 4)
        self.assertTupleEqual(np.shape(self.game_board.grid), (4, 4))
        self.assertTrue(np.all(self.game_board.grid == None))

    @input_cases({
        '4': 4,
        '9': 9,
        '-1': 3,
        'abc': 3,
        '2': 3,
        '10': 3,
        ' ': 3})
    def test_gather_board_size(self, expected_size):
        self.game_board.gather_board_size()

        self.assertEqual(self.game_board.size, expected_size)
        self.assertTupleEqual(np.shape(self.game_board.grid),
                              (expected_size, expected_size))
        self.assertTrue(np.all(self.game_board.grid == None))

    def test_render_at_start(self):
        render_result = self.game_board.render()

        self.assertEqual(render_result,
                         "    A   B   C   \n"
                         "1 | - | - | - | \n"
                         "2 | - | - | - | \n"
                         "3 | - | - | - | \n")

    def test_render_two_player_moves(self):
        self.game_board.make_player_move(0, 0, Player('Player1', 'X'))
        self.game_board.make_player_move(1, 1, Player('Player2', 'O'))

        render_result = self.game_board.render()

        self.assertEqual(render_result,
                         "    A   B   C   \n"
                         "1 | X | - | - | \n"
                         "2 | - | O | - | \n"
                         "3 | - | - | - | \n")

    def test_make_player_move_new_cell(self):
        player = Player('Player1', 'X')
        existing_player = self.game_board.make_player_move(0, 0, player)
        self.assertIsNone(existing_player)

    def test_make_player_move_existing_cell(self):
        player = Player('Player1', 'X')

        self.game_board.make_player_move(0, 0, player)
        existing_player = self.game_board.make_player_move(0, 0, player)

        self.assertEqual(existing_player, player)

    def test_check_win_state_at_start(self):
        winning_player, is_draw = self.game_board.check_win_state()
        self.assertTupleEqual((None, False), (winning_player, is_draw))

    def test_check_win_state_row_same(self):
        player = Player('Player1', 'X')

        self.game_board.make_player_move(0, 0, player)
        self.game_board.make_player_move(0, 1, player)
        self.game_board.make_player_move(0, 2, player)
        winning_player, is_draw = self.game_board.check_win_state()

        self.assertTupleEqual((player, False), (winning_player, is_draw))

    def test_check_win_state_column_same(self):
        player = Player('Player1', 'X')

        self.game_board.make_player_move(0, 0, player)
        self.game_board.make_player_move(1, 0, player)
        self.game_board.make_player_move(2, 0, player)
        winning_player, is_draw = self.game_board.check_win_state()

        self.assertTupleEqual((player, False), (winning_player, is_draw))

    def test_check_win_state_left_to_right_diagonal_same(self):
        player = Player('Player1', 'X')

        self.game_board.make_player_move(0, 0, player)
        self.game_board.make_player_move(1, 1, player)
        self.game_board.make_player_move(2, 2, player)
        winning_player, is_draw = self.game_board.check_win_state()

        self.assertTupleEqual((player, False), (winning_player, is_draw))

    def test_check_win_state_right_to_left_diagonal_same(self):
        player = Player('Player1', 'X')

        self.game_board.make_player_move(0, 2, player)
        self.game_board.make_player_move(1, 1, player)
        self.game_board.make_player_move(2, 0, player)
        winning_player, is_draw = self.game_board.check_win_state()

        self.assertTupleEqual((player, False), (winning_player, is_draw))

    def test_check_win_state_draw_state(self):
        player1 = Player('Player1', 'X')
        player2 = Player('Player1', 'O')

        self.game_board.make_player_move(0, 0, player1)
        self.game_board.make_player_move(0, 1, player2)
        self.game_board.make_player_move(1, 0, player1)
        self.game_board.make_player_move(2, 0, player2)
        self.game_board.make_player_move(1, 1, player1)
        self.game_board.make_player_move(2, 2, player2)
        self.game_board.make_player_move(2, 1, player1)
        self.game_board.make_player_move(1, 2, player2)
        self.game_board.make_player_move(0, 2, player1)

        winning_player, is_draw = self.game_board.check_win_state()
        self.assertTupleEqual((None, True), (winning_player, is_draw))


if __name__ == '__main__':
    unittest.main()
