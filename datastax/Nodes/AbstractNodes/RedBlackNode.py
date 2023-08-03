from typing import Self, Optional
from datastax.Nodes.AbstractNodes.TreeNode import TreeNode
from datastax.Utils import Commons, Colors
from abc import ABC as AbstractClass, abstractmethod

fore, back, reset = Colors.FORE, Colors.BACK, Colors.RESET
red, black, grey = Colors.RED, Colors.BLACK, Colors.GREY


class RedBlackNode(TreeNode, AbstractClass):
    _parent: Optional[Self] = None
    _color: int

    @property
    def parent(self):
        return self._parent

    @property
    def color(self):
        return self._color

    def __str__(self):
        values = list(
            map(
                lambda node: "" if node is None else Commons.format(
                    node.color, Commons.repr(node.data)
                ), [self, self.left, self.right]
            )
        )
        max_width = max(
            len(Commons.repr(data)) - 33 for data in values if data
        )
        max_width += max_width % 2  # To make max_width even
        padding = 4
        per_piece = 2 * (max_width + padding)
        extra_line = f"{back}{grey}{' ' * (per_piece + 1)}{reset}\n"

        string_builder = (
            f"{extra_line}"
            f"{back}{grey}"
            f"{Commons.redblack_node_builder(values[0], per_piece)} "
            f"{reset}\n{back}{grey}"
        )
        per_piece //= 2
        hpw = int(per_piece // 2 - 1)
        if any(values[1:]):
            if all(values[1:]):
                part = f"{' ' * (hpw + 1)}┌{'─' * hpw}┴{'─' * hpw}┐"
                string_builder += (
                    f"{part}{' ' * (len(part) - per_piece - 1)}"
                    f"{reset}\n{back}{grey}"
                )
                string_builder += Commons.redblack_node_builder(
                    values[1], per_piece
                ) + Commons.redblack_node_builder(
                    values[2], per_piece
                )
            elif values[1]:
                part = f"{' ' * (hpw + 1)}┌{'─' * hpw}┘ {' ' * hpw}"
                string_builder += (
                    f"{part}{' ' * (len(part) - per_piece - 1)}"
                    f"{reset}\n{back}{grey}"
                )
                string = Commons.redblack_node_builder(values[1], per_piece)
                string_builder += f"{string}{' ' * (len(string) - 33)}"
            else:
                part = f"{' ' * (per_piece - 1)} └{'─' * hpw}┐"
                string_builder += (
                    f"{part}{' ' * (len(part) - per_piece - 1)}"
                    f"{reset}\n{back}{grey}"
                )
                string_builder += (
                    f"{' ' * (per_piece - 1)} "
                    f"{Commons.redblack_node_builder(values[2], per_piece)}"
                )
        string_builder += f" {reset}\n{extra_line}"
        return string_builder

    def preorder_print(self) -> None:
        values = list(
            map(
                lambda node: "" if node is None else Commons.format(
                    node.color, Commons.repr(node.data)
                ), [self, self.left, self.right]
            )
        )
        string_builder = f'\n{back}{grey}{values[0]}  {reset}\n'
        if any(values[1:]):
            if all(values[1:]):
                string_builder += (
                    f"{back}{grey}├─▶ {values[1]}  {reset}\n"
                    f"{back}{grey}└─▶ {values[2]}  {reset}\n"
                )
            else:
                data = values[1] or values[2]
                string_builder += f"{back}{grey}└─▶ {data}  {reset}\n"

        print(string_builder)

    @abstractmethod
    def set_parent(self, parent: Self):
        ...

    @abstractmethod
    def set_color(self, color: int):
        ...
