"""Game constants."""

from typing import Literal

BOARD_SIZE: int = 3

ANSI_GREY: str = "\033[90m"
ANSI_RESET: str = "\033[0m"

MoveValue = Literal["X", "O"]
CellValue = MoveValue | None
