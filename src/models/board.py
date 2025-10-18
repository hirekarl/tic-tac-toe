"""Game board."""

from constants.constants import CellValue, BOARD_SIZE


class Board:
    """Game board."""

    _board: list[list[CellValue]]

    def __init__(self) -> None:
        self._board: list[list[CellValue]] = [
            [None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)
        ]

    def __str__(self) -> str:
        return "Board"

    def __repr__(self) -> str:
        return "Board()"

    def get_board(self) -> list[list[CellValue]]:
        board_copy: list[list[CellValue]] = [row[:] for row in self._board]
        return board_copy
