"""Game constants."""

from typing import Literal, Union

# Typing
MoveValue = Literal["X", "O"]
CellValue = Union[MoveValue, None]
CellKey = Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# NB: Do not change! Board size should *only* ever be 3.
BOARD_SIZE: int = 3

# ANSI Escape Sequences
ANSI_GREY: str = "\033[90m"
ANSI_RED: str = "\033[31m"
ANSI_GREEN: str = "\033[32m"
ANSI_RESET: str = "\033[0m"

# Board Grid Components
GRID_TOP: str = "   ╻   ╻   \n"
GRID_COL_JOINER: str = "┃"
GRID_ROW_JOINER: str = "\n━━━╋━━━╋━━━\n"
GRID_BOTTOM: str = "\n   ╹   ╹   "
