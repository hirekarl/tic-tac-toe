"""Color text as grey."""

import unittest

from constants.constants import ANSI_GREY, ANSI_RESET

from src.utils.grey import grey


class TestGrey(unittest.TestCase):
    """Test that grey() correctly bookends strings with correct ANSI escape sequences."""

    def test_grey_makes_grey_text(self) -> None:
        """Test that grey() correctly bookends strings with correct ANSI escape sequences."""

        test_string: str = "hello"
        self.assertEqual(grey(test_string), f"{ANSI_GREY}{test_string}{ANSI_RESET}")
