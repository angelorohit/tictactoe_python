from player import Player
from game_board import GameBoard


class GameCoordinator:
    def __init__(self) -> None:
        self.player1 = Player(name='Player 1', symbol='X')
        self.player2 = Player(name='Player 2', symbol='O')
        self.game_board = GameBoard(self.player1, self.player2)
        self.next_turn_player = self.player1

    def start(self) -> None:
        self.player1.gather_name()
        self.player2.gather_name()

        print('')
        print(f'{self.player1.name}\'s symbol is {self.player1.symbol}')
        print(f'{self.player2.name}\'s symbol is {self.player2.symbol}')
        print('')

        self.game_board.gather_board_size()
        print('')

        self.resume_game()

    def resume_game(self) -> None:
        self.game_board.render()

        winner, is_draw = self.game_board.check_win_state()
        if winner:
            print(f'{winner.name} wins!')
            return

        if is_draw:
            print('Draw!')
            return

        print(f'It is {self.next_turn_player.name}\'s turn.')
        row, col, error_msg = self.next_turn_player.take_turn(
            self.game_board.size)
        if error_msg:
            print(error_msg)
        else:
            existing_player = self.game_board.make_player_move(
                row, col, self.next_turn_player)
            if existing_player:
                print(f'{existing_player.name} has already played there!')
            else:
                self.next_turn_player = self.player2 if self.next_turn_player == self.player1 else self.player1

        self.resume_game()
