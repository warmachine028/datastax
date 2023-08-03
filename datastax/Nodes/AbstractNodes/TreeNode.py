from typing import Self, Any, Optional
from abc import ABC as AbstractClass, abstractmethod
from datastax.Utils import Commons


class TreeNode(AbstractClass):
    _left: Optional[Self]
    data: Any
    _right: Optional[Self]

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def __str__(self):
        values = [
            self.data if self.data is not None else str(None),
            self.left.data if self.left else None,
            self.right.data if self.right else None
        ]
        values = list(
            map(lambda value: Commons.repr(value), values)
        )
        max_width = max(len(Commons.repr(data)) for data in values if data)
        if max_width % 2:
            max_width += 1  # To make max_width even

        "Building string from calculated values"
        padding = 4
        per_piece = 2 * (max_width + padding)
        string_builder = f"{Commons.node_builder(values[0], per_piece)}\n"
        per_piece //= 2
        hpw = int(per_piece // 2 - 1)
        if self.left:
            if self.right:
                string_builder += (
                    f"{' ' * (hpw + 1)}"
                    f"┌{'─' * hpw}┴{'─' * hpw}┐\n"
                )
                string_builder += Commons.node_builder(
                    values[1], per_piece
                ) + Commons.node_builder(values[2], per_piece)
            else:
                string_builder += f"{' ' * (hpw + 1)}┌{'─' * hpw}┘\n"
                string_builder += Commons.node_builder(values[1], per_piece)
        elif self.right:
            string_builder += f"{' ' * (per_piece - 1)} └{'─' * hpw}┐\n"
            string_builder += (
                f"{' ' * (per_piece - 1)} "
                f"{Commons.node_builder(values[2], per_piece)}"
            )

        return string_builder

    def preorder_print(self) -> None:
        values = [
            self.data if self.data is not None else str(None),
            self.left.data if self.left else None,
            self.right.data if self.right else None
        ]
        values = list(
            map(
                lambda value: None if value is None else Commons.repr(value),
                values
            )
        )

        string_builder = f'{values[0]}\n'
        if self.left or self.right:
            if self.left and self.right:
                string_builder += f"├─▶ {values[1]}\n"
                string_builder += f"└─▶ {values[2]}"
            else:
                string_builder += f"└─▶ {values[1] or values[2]}"

        print(string_builder)

    @abstractmethod
    def set_left(self, left: Self):
        ...

    @abstractmethod
    def set_right(self, right: Self):
        ...
