"""CLI Tic-Tac-Toe."""

from src.models.board import Board

from .game_loop import display_title, loop_game


def main() -> None:
    """Game execution."""

    board: Board = Board()

    display_title()
    loop_game(board)


if __name__ == "__main__":
    main()
