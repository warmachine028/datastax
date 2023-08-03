from typing import Any, Optional
import math
from datastax.Utils.ColorCodes import ColorCodes
from datastax.Utils.Colors import Colors


class Commons:
    @staticmethod
    def repr(item: Any) -> str:
        if "\n" in str(item):
            return f"{str(type(item))[8:-2].split('.')[-1]}@{id(item)}"
        return str(item)

    @staticmethod
    def node_builder(data: Optional[str], piece_width: int) -> str:
        value = data or ''
        gap1 = int(math.ceil(piece_width / 2 - len(value) / 2))
        gap2 = int(math.floor(piece_width / 2 - len(value) / 2))
        return f"{' ' * gap1}{value}{' ' * gap2}"

    @staticmethod
    def format(color, data):
        fore, back = Colors.FORE, Colors.BACK
        red, black, grey = Colors.RED, Colors.BLACK, Colors.GREY
        if color is ColorCodes.BLACK:
            return f"{fore}{red}{back}{black}  {data}  {back}{grey}"
        return f"{fore}{black}{back}{red}  {data}  {back}{grey}"

    @staticmethod
    def redblack_node_builder(data: Optional[str],
                              piece_width: int, n: int = 0) -> str:
        value: str = data or ''
        n = n or len(value) - 33 if value else 0

        gap1 = int(math.ceil(piece_width / 2 - n / 2))
        gap2 = int(math.floor(piece_width / 2 - n / 2))
        return f"{' ' * gap1}{value}{' ' * gap2}"
