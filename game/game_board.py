from player import Player
from typing import Optional


class GameBoard:
    def __init__(self, player1: Player, player2: Player, size: int = 3):
        self.empty_cell_symbol = '-'
        self.clear(size)

    def gather_board_size(self):
        size = input('Enter a game board size between 3 and 9 (inclusive): ')
        if size.isdigit() and int(size) >= 3 and int(size) <= 9:
            self.clear(int(size))
        else:
            print(
                f'The game board size must be between 3 and 9 (inclusive). Defaulting to {self.size}')

    def clear(self, size: int) -> None:
        self.size = size
        self.grid = tuple([None for pos in range(0, size)]
                          for row in range(0, size))

    def render(self) -> None:
        # Print all the column labels
        print(end='    ')
        upper_a_ascii = ord('A')
        for col in range(0, self.size):
            print(f'{chr(upper_a_ascii + col)}', end='   ')
        print()

        # Print row labels along with cells for each row
        for row_index, row in enumerate(self.grid):
            print(f'{row_index + 1} |', end=' ')
            for player in row:
                print(
                    f'{self.empty_cell_symbol if player == None else player.symbol} |', end=' ')
            print()

    def make_player_move(self, row: int, col: int, player: Player) -> Optional[Player]:
        existing_player = self.grid[row][col]
        if not existing_player:
            self.grid[row][col] = player

        return existing_player

    def check_win_state(self) -> (Optional[Player], bool):
        all_items_same = (lambda items: all(
            item and item == items[0] for item in items))

        # Make transposed matrix of grid to check columns
        # TODO: Look into using numpy for better readability
        transposed_grid = tuple(zip(*self.grid))

        for pos in range(0, self.size):
            # Check rows
            if all_items_same(self.grid[pos]):
                return self.grid[pos][0], False

            # Check columns
            if all_items_same(transposed_grid[pos]):
                return transposed_grid[pos][0], False

        # Make and check left-to-right diagonal tuple
        left_to_right_diagonal = tuple(row[index]
                                       for index, row in enumerate(self.grid))
        if all_items_same(left_to_right_diagonal):
            return left_to_right_diagonal[0], False

        # Make and check right-to-left diagonal tuple
        right_to_left_diagonal = tuple(row[-index - 1]
                                       for index, row in enumerate(self.grid))
        if all_items_same(right_to_left_diagonal):
            return right_to_left_diagonal[0], False

        # If all cells are filled, then the game is a draw
        is_draw = all(all(player for player in self.grid[pos]) for pos in range(
            0, self.size))
        return None, is_draw
