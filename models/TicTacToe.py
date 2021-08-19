from exceptions.GameException import InvalidPositionException
from models.Board import Board
from models.GameState import GameState
from models.Player import Player


class TicTacToe:
    def __init__(self, player_1, player_2, board):
        self._player_1: Player = player_1
        self._player_2: Player = player_2
        self._board: Board = board
        self._current_player: Player = self._player_1
        self.status: GameState = GameState.ONGOING

    def play(self):
        self._board.display()
        self._board.show_options()

        cell_number = input("Choice: ")
        if not self._board.is_valid(cell_number):
            raise InvalidPositionException('Invalid cell_number')

        self._board.place_marker(cell_number=int(cell_number), marker=self._current_player.marker)

        if self._has_winner():
            self._update_state_to(GameState.ENDED)
            return

        if self._is_draw():
            self._update_state_to(GameState.DRAW)
            return

        self._swap_player()

    def declare_results(self):
        if self.status == GameState.DRAW:
            print('It is a draw')
            return

        print('{} has won the game'.format(self._current_player))

    def _has_winner(self):
        return self._board.has_consecutive_marker_on_columns() \
               or self._board.has_consecutive_marker_on_rows() \
               or self._board.has_consecutive_marker_on_diagonal()

    def _swap_player(self):
        if self._current_player == self._player_1:
            self._current_player = self._player_2
        else:
            self._current_player = self._player_1

    def _is_draw(self):
        return self._board.is_full()

    def _update_state_to(self, game_state: GameState):
        self.status = game_state
