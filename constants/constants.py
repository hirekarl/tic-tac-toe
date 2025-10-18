"""Game constants."""

from typing import Literal

BOARD_SIZE: int = 3

MoveValue = Literal["X", "O"]
CellValue = MoveValue | None
