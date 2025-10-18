"""Turn text grey."""

from constants.constants import ANSI_GREY, ANSI_RESET


def grey(input_str: str) -> str:
    """Turn text grey."""

    return f"{ANSI_GREY}{input_str}{ANSI_RESET}"
