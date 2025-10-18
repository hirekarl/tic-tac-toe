"""Test suite for Board."""

import unittest

from src.models.board import Board, InvalidCellLocationError
from constants.constants import CellValue, BOARD_SIZE


class TestBoardGetBoard(unittest.TestCase):
    """Test Board.get_board implementation."""

    def setUp(self) -> None:
        self.board = Board()

    def test_get_board_returns_correctly_sized_board(self) -> None:
        """Test that the Board.get_board returns a board of the correct dimensions."""

        board: list[list[CellValue]] = self.board.get_board()

        self.assertEqual(len(board), BOARD_SIZE)
        for row in board:
            self.assertEqual(len(row), BOARD_SIZE)


class TestBoardGetCell(unittest.TestCase):
    """Test Board.get_cell implementation."""

    def setUp(self) -> None:
        test_board_state: list[list[CellValue]] = [
            ["X", "O", None],
            ["O", None, "X"],
            [None, "X", "O"],
        ]
        self.board = Board(board_state=test_board_state)

    def test_get_cell_raises_invalid_cell_location_error_if_invalid_cell_location_provided(
        self,
    ) -> None:
        """Test that Board.get_cell raises InvalidCellLocationError
        if invalid cell location provided."""

        with self.assertRaises(InvalidCellLocationError):
            self.board.get_cell(-1, 0)

        with self.assertRaises(InvalidCellLocationError):
            self.board.get_cell(0, -1)

        with self.assertRaises(InvalidCellLocationError):
            self.board.get_cell(BOARD_SIZE + 1, 0)

        with self.assertRaises(InvalidCellLocationError):
            self.board.get_cell(0, BOARD_SIZE + 1)

    def test_get_cell_returns_correct_value_if_valid_cell_location_provided(
        self,
    ) -> None:
        """Test that Board.get_cell returns correct value
        if valid cell location provided."""

        self.assertEqual(self.board.get_cell(0, 0), "X")
        self.assertEqual(self.board.get_cell(1, 1), None)
        self.assertEqual(self.board.get_cell(2, 2), "O")
