from typing import Optional


class Player:
    def __init__(self, name: str, symbol: str) -> None:
        self.name = name
        self.symbol = symbol

    def gather_name(self) -> None:
        name = input(f'Enter {self.name} name: ').strip()
        if name:
            self.name = name
        else:
            print(f'Your name cannot be empty. Defaulting to {self.name}')

    def take_turn(self, grid_size: int) -> (int, int, str):
        turn_input = input('Enter your position (Example, A1 or C2): ')
        return self.validate_turn_input(turn_input, grid_size)

    def validate_turn_input(self, turn_input: str, game_board_size: int) -> (int, int, Optional[str]):
        if len(turn_input) != 2:
            return 0, 0, 'You must enter a position as the letter column and number row. Example, A1 or C2'

        col = turn_input[0]
        row = turn_input[1]

        if not row.isdigit or not col.isalpha:
            return 0, 0, 'You must enter a position as the letter column and number row. Example, A1 or C2'

        row_pos = int(row) - 1
        if row_pos >= game_board_size:
            return 0, 0, f'You must enter a row value that is within the playing grid size of 1 to {game_board_size}'

        upper_a_ascii = ord('A')
        col_pos = ord(col.upper()) - upper_a_ascii

        if col_pos >= game_board_size:
            return 0, 0, f'You must enter a column value that is within the playing grid size of A to {chr(upper_a_ascii + game_board_size - 1)}'

        return row_pos, col_pos, None
