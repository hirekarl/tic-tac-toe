"""Test suite for Board."""

import unittest

from src.models.board import Board
from constants.constants import CellValue, BOARD_SIZE


class TestBoardGetBoard(unittest.TestCase):
    """test Board.get_board implementation."""

    def setUp(self) -> None:
        self.board = Board()

    def test_get_board_returns_correctly_sized_board(self) -> None:
        """Test that the Board.get_board returns a board of the correct dimensions."""

        board: list[list[CellValue]] = self.board.get_board()

        self.assertEqual(len(board), BOARD_SIZE)
        for row in board:
            self.assertEqual(len(row), BOARD_SIZE)
