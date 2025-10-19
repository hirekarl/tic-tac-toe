"""Test suite for text colorization utilities."""

import unittest

from constants.constants import ANSI_GREY, ANSI_RED, ANSI_GREEN, ANSI_RESET

from src.utils.colorize import grey, red, green


class TestColorize(unittest.TestCase):
    """Test that colorize functions correctly bookend strings with correct ANSI escape sequences."""

    def setUp(self) -> None:
        self.test_string: str = "Hello, World!"

    def test_grey_makes_grey_text(self) -> None:
        """Test that `grey` correctly creates grey text."""

        self.assertEqual(
            grey(self.test_string), f"{ANSI_GREY}{self.test_string}{ANSI_RESET}"
        )

    def test_red_makes_red_text(self) -> None:
        """Test that `red` correctly creates red text."""

        self.assertEqual(
            red(self.test_string), f"{ANSI_RED}{self.test_string}{ANSI_RESET}"
        )

    def test_green_makes_green_text(self) -> None:
        """Test that `green` correctly creates green text."""

        self.assertEqual(
            green(self.test_string), f"{ANSI_GREEN}{self.test_string}{ANSI_RESET}"
        )
