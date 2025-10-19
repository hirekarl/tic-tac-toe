"""Test suite for Board."""

import unittest

from copy import deepcopy
from typing import List

from constants.constants import CellValue, BOARD_SIZE

from src.models.board import Board, InvalidCellError, InvalidMoveError

from src.utils.colorize import grey, red, green


# NB: Do not change! Test cases depend on this.
TEST_BOARD_STATE: List[List[CellValue]] = [
    ["X", "O", None],
    ["O", None, "X"],
    [None, "X", "O"],
]


class TestBoardGetBoard(unittest.TestCase):
    """Test Board.get_board implementation."""

    def setUp(self) -> None:
        self.board = Board()

    def test_get_board_returns_correctly_sized_board(self) -> None:
        """Test that the Board.get_board returns a board of the correct dimensions."""

        board: List[List[CellValue]] = self.board.get_board()

        self.assertEqual(len(board), BOARD_SIZE)
        for row in board:
            self.assertEqual(len(row), BOARD_SIZE)


class TestBoardGetCell(unittest.TestCase):
    """Test Board.get_cell implementation."""

    def setUp(self) -> None:
        test_board_state: List[List[CellValue]] = deepcopy(TEST_BOARD_STATE)
        self.board = Board(starting_state=test_board_state)

    def test_get_cell_raises_invalid_cell_error_if_invalid_cell_provided(
        self,
    ) -> None:
        """Test that Board.get_cell raises InvalidCellError
        if invalid cell provided."""

        with self.assertRaises(InvalidCellError):
            self.board.get_cell(-1, 0)

        with self.assertRaises(InvalidCellError):
            self.board.get_cell(0, -1)

        with self.assertRaises(InvalidCellError):
            self.board.get_cell(BOARD_SIZE + 1, 0)

        with self.assertRaises(InvalidCellError):
            self.board.get_cell(0, BOARD_SIZE + 1)

    def test_get_cell_returns_correct_value_if_valid_cell_provided(
        self,
    ) -> None:
        """Test that Board.get_cell returns correct value
        if valid cell provided."""

        self.assertEqual(self.board.get_cell(0, 0), "X")
        self.assertEqual(self.board.get_cell(1, 1), None)
        self.assertEqual(self.board.get_cell(2, 2), "O")


class TestBoardMakeMove(unittest.TestCase):
    """Test Board.make_move implementation."""

    def setUp(self) -> None:
        test_board_state: List[List[CellValue]] = deepcopy(TEST_BOARD_STATE)
        self.board = Board(starting_state=test_board_state)

    def test_make_move_raises_invalid_cell_error_if_invalid_cell_attempted(
        self,
    ) -> None:
        """Tests that Board.make_move raises InvalidCellError
        if an attempt is made to play on an invalid cell."""

        with self.assertRaises(InvalidCellError):
            self.board.make_move(-1, 0, "X")

        with self.assertRaises(InvalidCellError):
            self.board.make_move(0, BOARD_SIZE + 1, "O")

    def test_make_move_raises_invalid_move_error_if_nonblank_cell_attempted(
        self,
    ) -> None:
        """Tests that Board.make_move raises InvalidMoveError
        if an attempt is made to play on a nonblank cell."""

        with self.assertRaises(InvalidMoveError):
            self.board.make_move(0, 0, "O")

        with self.assertRaises(InvalidMoveError):
            self.board.make_move(2, 2, "X")

    def test_make_move_raises_invalid_move_error_if_invalid_move_attempted(
        self,
    ) -> None:
        """Tests that Board.make_move raises InvalidMoveError
        if an attempt is made to play a move other than "X" or "O"."""

        with self.assertRaises(InvalidMoveError):
            self.board.make_move(0, 2, "Y")  # type: ignore

    def test_make_move_correctly_changes_board_state(self) -> None:
        """Tests that Board.make_move correctly changes board state
        when called."""

        self.board.make_move(0, 2, "X")
        self.assertEqual(self.board.get_cell(0, 2), "X")

        self.board.make_move(1, 1, "O")
        self.assertEqual(self.board.get_cell(1, 1), "O")


class TestBoardStringifyBoard(unittest.TestCase):
    """Tests that Board.stringify_board returns the correct string."""

    def setUp(self) -> None:
        test_board_state: List[List[CellValue]] = deepcopy(TEST_BOARD_STATE)
        self.board = Board(starting_state=test_board_state)

    def test_stringify_board_returns_proper_board_string(self) -> None:
        """Tests that Board.stringify_board returns the correct string."""

        actual_board_string = self.board.stringify_board()

        top: str = "   ╻   ╻   "
        row1: str = f"{red(' X ')}┃{green(' O ')}┃{grey(' 9 ')}"
        joiner: str = "━━━╋━━━╋━━━"
        row2: str = f"{green(' O ')}┃{grey(' 5 ')}┃{red(' X ')}"
        row3: str = f"{grey(' 1 ')}┃{red(' X ')}┃{green(' O ')}"
        bottom: str = "   ╹   ╹   "

        correct_board_string: str = (
            f"{top}\n{row1}\n{joiner}\n{row2}\n{joiner}\n{row3}\n{bottom}"
        )

        self.assertEqual(actual_board_string, correct_board_string)
