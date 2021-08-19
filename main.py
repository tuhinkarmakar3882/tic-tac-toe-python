from exceptions import GameException
from models.Board import Board
from models.GameState import GameState
from models.Player import Player
from models.TicTacToe import TicTacToe

if __name__ == "__main__":
    first_player = Player(name="Player 1", marker="X")
    second_player = Player(name="Player 2", marker="O")

    tic_tac_toe_board = Board(size=3)

    game = TicTacToe(
        player_1=first_player,
        player_2=second_player,
        board=tic_tac_toe_board
    )

    while game.status == GameState.ONGOING:
        try:
            game.play()
        except GameException.InvalidPositionException:
            print('\n[!] Invalid Input. Try Again!')

    game.declare_results()
