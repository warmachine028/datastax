from dataclasses import dataclass


@dataclass
class Colors:
    BLACK: str = '\x1B[38;5;232m'
    RED: str = '\x1B[38;5;196m'
    GREY: str = '\x1B[38;5;237m'
    FORE: str = '\x1B[38;5;'
    BACK: str = '\x1B[48;5;'
    RESET: str = '\x1b[0m'
