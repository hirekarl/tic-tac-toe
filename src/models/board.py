"""Game board."""

from copy import deepcopy
from typing import List

from constants.constants import (
    MoveValue,
    CellValue,
    BOARD_SIZE,
    GRID_TOP,
    GRID_COL_JOINER,
    GRID_ROW_JOINER,
    GRID_BOTTOM,
)

from src.utils.colorize import grey, red, green


class InvalidCellError(Exception):
    """Custom error for when an invalid cell is requested."""

    _message: str

    def __init__(self, message: str = "Invalid cell."):
        self._message: str = message
        super().__init__(self._message)


class InvalidMoveError(Exception):
    """Custom error for when an invalid move is attempted."""

    _message: str

    def __init__(self, message: str = "Invalid move."):
        self._message: str = message
        super().__init__(self._message)


BLANK_BOARD: List[List[CellValue]] = [
    [None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)
]

VALID_MOVES: List[MoveValue] = ["X", "O"]


class Board:
    """Game board."""

    _board: List[List[CellValue]]

    def __init__(
        self, starting_state: List[List[CellValue]] = deepcopy(BLANK_BOARD)
    ) -> None:
        self._board: List[List[CellValue]] = starting_state

    def __str__(self) -> str:
        return "Board"

    def __repr__(self) -> str:
        return "Board()"

    def _is_valid_cell(self, row: int, col: int) -> bool:
        return 0 <= row <= BOARD_SIZE and 0 <= col <= BOARD_SIZE

    def _is_blank_cell(self, row: int, col: int) -> bool:
        return self._board[row][col] is None

    def get_board(self) -> List[List[CellValue]]:
        """Get a copy of the game board state.

        Returns:
            List[List[CellValue]]: A copy of the game board state.
        """

        board_copy: List[List[CellValue]] = [row[:] for row in self._board]
        return board_copy

    def get_cell(self, row: int, col: int) -> CellValue:
        """Get the value at (`row`, `col`) from the board.

        Args:
            row (int): Row number (0-indexed).
            col (int): Column number (0-indexed).

        Raises:
            InvalidCellError: When an invalid (`row`, `col`) is requested.

        Returns:
            CellValue: The value at (`row`, `col`).
        """

        if not self._is_valid_cell(row, col):
            raise InvalidCellError(f"({row}, {col}) is not a valid cell.")

        cell_value: CellValue = self._board[row][col]
        return cell_value

    def make_move(self, row: int, col: int, move_value: MoveValue) -> None:
        """Play `move_value` at (`row`, `col`).

        Args:
            row (int): Row number (0-indexed).
            col (int): Column number (0-indexed).
            move_value (MoveValue): "X" or "O".

        Raises:
            InvalidCellError: When an attempt is made to play on an invalid cell.
            InvalidMoveError: When an attempt is made to play on a nonblank cell.
            InvalidMoveError: When an attempt is made to play a move other than "X" or "O".
        """

        if not self._is_valid_cell(row, col):
            raise InvalidCellError(f"({row}, {col}) is not a valid cell.")

        if not self._is_blank_cell(row, col):
            raise InvalidMoveError(
                f"{self._board[row][col]!r} already played at ({row}, {col})."
            )

        if not move_value in VALID_MOVES:
            raise InvalidMoveError(f"Invalid move: {move_value!r}.")

        self._board[row][col] = move_value

    def stringify_board(self) -> str:
        """Turn the board into a string for display."""

        rows: List[str] = []
        for row in range(BOARD_SIZE):
            cols: List[str] = []

            for col in range(BOARD_SIZE):
                value: CellValue = self.get_cell(row, col)
                cell_display: str = ""

                match value:
                    case None:
                        match row:
                            case 0:
                                cell_display = grey(f" {row + 7 + col} ")
                            case 1:
                                cell_display = grey(f" {row + 3 + col} ")
                            case 2:
                                cell_display = grey(f" {row - 1 + col} ")
                            case _:
                                raise ValueError(f"Invalid row number: {row!r}.")

                    case "X":
                        cell_display = red(" X ")
                    case "O":
                        cell_display = green(" O ")
                    case _:
                        raise ValueError(f"Invalid value: {value!r}.")

                cols.append(cell_display)

            row_display: str = GRID_COL_JOINER.join(cols)
            rows.append(row_display)

        board_display: str = f"{GRID_TOP}{GRID_ROW_JOINER.join(rows)}{GRID_BOTTOM}"
        return board_display
