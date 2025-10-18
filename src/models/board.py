"""Game board."""

from constants.constants import BOARD_SIZE, MoveValue, CellValue


class InvalidCellError(Exception):
    """Custom error for when an invalid cell location is requested."""

    _message: str

    def __init__(self, message: str = "Invalid cell location."):
        self._message: str = message
        super().__init__(self._message)


class InvalidMoveError(Exception):
    """Custom error for when an invalid move is attempted."""

    _message: str

    def __init__(self, message: str = "Invalid move."):
        self._message: str = message
        super().__init__(self._message)


BLANK_BOARD: list[list[CellValue]] = [
    [None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)
]

VALID_MOVES: list[MoveValue] = ["X", "O"]


class Board:
    """Game board."""

    _board: list[list[CellValue]]

    def __init__(self, starting_state: list[list[CellValue]] = BLANK_BOARD) -> None:
        self._board: list[list[CellValue]] = starting_state

    def __str__(self) -> str:
        return "Board"

    def __repr__(self) -> str:
        return "Board()"

    def _is_valid_cell(self, row: int, col: int) -> bool:
        return 0 <= row <= BOARD_SIZE and 0 <= col <= BOARD_SIZE

    def _is_blank_cell(self, row: int, col: int) -> bool:
        return self._board[row][col] is None

    def get_board(self) -> list[list[CellValue]]:
        """Get a copy of the game board state.

        Returns:
            list[list[CellValue]]: A copy of the game board state.
        """

        board_copy: list[list[CellValue]] = [row[:] for row in self._board]
        return board_copy

    def get_cell(self, row: int, col: int) -> CellValue:
        """Get the value at location (`row`, `col`) from the board.

        Args:
            row (int): Row number (0-indexed).
            col (int): Column number (0-indexed).

        Raises:
            InvalidCellError: When an invalid (`row`, `col`) is requested.

        Returns:
            CellValue: The value at location (`row`, `col`).
        """

        if not self._is_valid_cell(row, col):
            raise InvalidCellError(f"({row}, {col}) is not a valid cell location.")

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
        """

        if not self._is_valid_cell(row, col):
            raise InvalidCellError(f"({row}, {col}) is not a valid cell location.")

        if not self._is_blank_cell(row, col):
            raise InvalidMoveError(
                f"{self._board[row][col]!r} already played at ({row}, {col})."
            )

        self._board[row][col] = move_value
