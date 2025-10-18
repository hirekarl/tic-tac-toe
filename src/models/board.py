"""Game board."""

from constants.constants import CellValue, BOARD_SIZE


BLANK_BOARD: list[list[CellValue]] = [
    [None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)
]


class Board:
    """Game board."""

    _board: list[list[CellValue]]

    def __init__(self, board_state: list[list[CellValue]] = BLANK_BOARD) -> None:
        self._board: list[list[CellValue]] = board_state

    def __str__(self) -> str:
        return "Board"

    def __repr__(self) -> str:
        return "Board()"

    def _is_valid_cell_location(self, row: int, col: int) -> bool:
        return 0 <= row <= BOARD_SIZE and 0 <= col <= BOARD_SIZE

    def get_board(self) -> list[list[CellValue]]:
        """Get a copy of the game board state.

        Returns:
            list[list[CellValue]]: A copy of the game board state.
        """

        board_copy: list[list[CellValue]] = [row[:] for row in self._board]
        return board_copy
