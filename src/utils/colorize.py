"""Turn text grey."""

from constants.constants import ANSI_GREY, ANSI_RED, ANSI_GREEN, ANSI_RESET


def grey(input_str: str) -> str:
    """Turn text grey."""

    return f"{ANSI_GREY}{input_str}{ANSI_RESET}"


def red(input_str: str) -> str:
    """Turn text red."""

    return f"{ANSI_RED}{input_str}{ANSI_RESET}"


def green(input_str: str) -> str:
    """Turn text green."""

    return f"{ANSI_GREEN}{input_str}{ANSI_RESET}"
