from typing import Optional

import numpy as np

from game.player import Player


class GameBoard:
    def __init__(self, size: int = 3):
        self.empty_cell_symbol = '-'
        self.clear(size)

    def gather_board_size(self):
        size = input(
            'Enter a game board size between 3 and 9 (inclusive): ').strip()
        if size.isdigit() and int(size) >= 3 and int(size) <= 9:
            self.clear(int(size))
        else:
            self.clear(size=3)
            print(
                f'The game board size must be between 3 and 9 (inclusive). Defaulting to 3')

    def clear(self, size: int) -> None:
        self.size = size
        self.grid = np.empty(shape=(size, size), dtype=Player)

    def render(self) -> str:
        # Print all the column labels
        render_result = '    '
        col_start_ascii = ord('A')
        for col_ascii in range(col_start_ascii, col_start_ascii + self.size):
            render_result += f'{chr(col_ascii)}   '
        render_result += '\n'

        # Print row labels along with cells for each row
        row_label = 1
        for row in self.grid:
            render_result += f'{row_label} | '
            for player in row:
                render_result += f'{self.empty_cell_symbol if player == None else player.symbol} | '
            render_result += '\n'
            row_label += 1
        return render_result

    def make_player_move(self, row: int, col: int, player: Player) -> Optional[Player]:
        existing_player = self.grid[row][col]
        if not existing_player:
            self.grid[row][col] = player

        return existing_player

    def check_win_state(self) -> (Optional[Player], bool):
        all_items_same = (lambda items: all(
            item and item == items[0] for item in items))

        # Make transposed matrix of grid to check columns
        transposed_grid = np.transpose(self.grid)

        for pos in range(0, self.size):
            # Check rows
            if all_items_same(self.grid[pos]):
                return self.grid[pos][0], False

            # Check columns
            if all_items_same(transposed_grid[pos]):
                return transposed_grid[pos][0], False

        left_to_right_diagonal = np.diagonal(self.grid)
        if all_items_same(left_to_right_diagonal):
            return left_to_right_diagonal[0], False

        right_to_left_diagonal = np.diagonal(np.fliplr(self.grid))
        if all_items_same(right_to_left_diagonal):
            return right_to_left_diagonal[0], False

        is_draw = np.all(self.grid != None)

        return None, is_draw
