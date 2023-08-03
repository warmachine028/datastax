from datastax.Nodes.AbstractNodes.TreeNode import TreeNode
from datastax.Utils import Commons
from abc import ABC as AbstractClass, abstractmethod


class HuffmanNode(TreeNode, AbstractClass):
    _frequency: int

    @property
    def frequency(self):
        return self._frequency

    def __str__(self):
        values = [
            self.data or self.frequency,
            self.left.data or self.left.frequency if self.left else None,
            self.right.data or self.right.frequency if self.right else None,
        ]
        values = list(
            map(
                lambda value: "" if value is None else Commons.repr(value),
                values
            )
        )
        max_width = max(len(Commons.repr(data)) for data in values if data)
        if max_width % 2:
            max_width += 1  # To make max_width even

        "Building string from calculated values"
        per_piece = 2 * (max_width + 4)
        string_builder = f"{Commons.node_builder(values[0], per_piece)}\n"
        per_piece //= 2
        hpw = int(per_piece // 2 - 1)
        if any(values[1:]):
            if all(values[1:]):
                string_builder += (
                    f"{' ' * (hpw + 1)}" f"┌{'─' * hpw}┴{'─' * hpw}┐\n"
                )
                string_builder += (
                        Commons.node_builder(values[1], per_piece)
                        + Commons.node_builder(values[2], per_piece)
                )
            elif values[1]:
                string_builder += f"{' ' * (hpw + 1)}┌{'─' * hpw}┘\n"
                string_builder += Commons.node_builder(values[1], per_piece)
            else:
                string_builder += f"{' ' * (per_piece - 1)} └{'─' * hpw}┐\n"
                string_builder += (
                    f"{' ' * (per_piece - 1)} "
                    f"{Commons.node_builder(values[2], per_piece)}"
                )

        return string_builder

    def preorder_print(self) -> None:
        values = [
            self.data or self.frequency,
            self.left.data or self.left.frequency if self.left else None,
            self.right.data or self.right.frequency if self.right else None,
        ]
        values = list(
            map(
                lambda value: "" if value is None else Commons.repr(value),
                values
            )
        )

        string_builder = f"{values[0]}\n"
        if any(values[1:]):
            if all(values[1:]):
                string_builder += f"├─▶ {values[1]}\n"
                string_builder += f"└─▶ {values[2]}"
            else:
                string_builder += f"└─▶ {values[1] or values[2]}"

        print(string_builder)

    @abstractmethod
    def set_frequency(self, frequency: int):
        ...
