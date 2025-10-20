"""Main game loop functions."""

import sys

from typing import Union, cast

from constants.constants import PlayerMarker

from src.models.board import Board

from src.ui.prompts import prompt

from src.utils.colorize import magenta, yellow


def _end_game(board: Board, winner: Union[PlayerMarker, None]) -> None:
    """End game if result is a draw or win."""

    print(f"\n{board.stringify_board()}")

    if winner is None:
        print(f"\n{yellow('   Draw!   ')}\n")
    else:
        print(f"\n{yellow(f'  {winner} wins!  ')}\n")

    sys.exit(0)


def display_title() -> None:
    """Display game title."""

    print(magenta("\nTIC-TAC-TOE"))


def loop_game(board: Board) -> None:
    """Execute main game loop."""

    player: PlayerMarker | None = None

    win, winner = board.check_win()

    while not win and winner is None:
        if board.check_draw():
            _end_game(board, None)

        player = "X" if player == "O" or player is None else "O"
        prompt(player, board)

        win, winner = board.check_win()

    winner = cast(PlayerMarker, winner)
    _end_game(board, winner)
