from __future__ import annotations

import math
from itertools import chain
from typing import Any, Optional

from datastax.trees.private_trees.binary_tree import (
    TreeNode,
    BinaryTree,
    _mangled,
)

RED = 0
BLACK = 1

black, red, grey = '232m', '196m', '237m'
fore, back, reset = '\x1B[38;5;', '\x1B[48;5;', '\x1b[0m'


def _node_builder(data: Optional[str], piece_width: int, n: int = 0) -> str:
    value: str = data or ''
    n = n or len(value) - 33 if value else 0

    gap1 = int(math.ceil(piece_width / 2 - n / 2))
    gap2 = int(math.floor(piece_width / 2 - n / 2))
    return f"{' ' * gap1}{value}{' ' * gap2}"


def _format(color, data):
    if color is BLACK:
        return f"{fore}{red}{back}{black}  {data}  {back}{grey}"
    return f"{fore}{black}{back}{red}  {data}  {back}{grey}"


class RedBlackNode(TreeNode):
    def __init__(self, data: Any,
                 left: RedBlackNode = None,
                 right: RedBlackNode = None,
                 color: int = RED):
        super().__init__(data, left, right)
        self.parent: Optional[RedBlackNode] = None
        self.color = color

    def __str__(self):
        values = list(
            map(
                lambda node: "" if node is None else _format(
                    node.color, _mangled(node.data)
                ), [self, self.left, self.right]
            )
        )
        max_width = max(len(_mangled(data)) - 33 for data in values if data)
        max_width += max_width % 2  # To make max_width even
        padding = 4
        per_piece = 2 * (max_width + padding)
        extra_line = f"{back}{grey}{' ' * (per_piece + 1)}{reset}\n"

        string_builder = (
            f"{extra_line}"
            f"{back}{grey}{_node_builder(values[0], per_piece)} "
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
                string_builder += _node_builder(
                    values[1], per_piece
                ) + _node_builder(
                    values[2], per_piece
                )
            elif values[1]:
                part = f"{' ' * (hpw + 1)}┌{'─' * hpw}┘ {' ' * hpw}"
                string_builder += (
                    f"{part}{' ' * (len(part) - per_piece - 1)}"
                    f"{reset}\n{back}{grey}"
                )
                string = _node_builder(values[1], per_piece)
                string_builder += f"{string}{' ' * (len(string) - 33)}"
            else:
                part = f"{' ' * (per_piece - 1)} └{'─' * hpw}┐"
                string_builder += (
                    f"{part}{' ' * (len(part) - per_piece - 1)}"
                    f"{reset}\n{back}{grey}"
                )
                string_builder += (
                    f"{' ' * (per_piece - 1)} "
                    f"{_node_builder(values[2], per_piece)}"
                )
        string_builder += f" {reset}\n{extra_line}"
        return string_builder

    def preorder_print(self) -> str:
        values = list(
            map(
                lambda node: "" if node is None else _format(
                    node.color, _mangled(node.data)
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

        return string_builder


class RedBlackTree(BinaryTree):
    def insert(self, item: Any):
        raise NotImplementedError

    @staticmethod
    def _nodes_level_wise(root: RedBlackNode) -> list[list]:
        level: list = [root]
        nodes: int = 1
        levels: list[list] = []
        while nodes:
            current_level: list[Optional[RedBlackNode]] = []
            next_level = []
            nodes = 0
            for node in level:
                if not node:
                    current_level.append(None)
                    next_level += [None] * 2
                    continue
                current_level.append(node)
                next_level += [node.left, node.right]
                if node.left:
                    nodes += 1
                if node.right:
                    nodes += 1
            levels.append(current_level)
            level = next_level
        return levels

    @staticmethod
    def _maximum_width(levels: list[list]) -> int:
        max_width = 0
        for node in filter(bool, chain(*levels)):
            data = _mangled(node.data)
            max_width = max(max_width, len(data) + 4)
        return max_width + 1 if max_width % 2 else max_width

    # Level order Traversal of Tree
    def __str__(self):  # noqa: C901
        # return super().__str__()
        root = self.root
        if not root:
            return "  NULL"
        levels = self._nodes_level_wise(root)
        max_width = self._maximum_width(levels) + 1
        padding = 4
        per_piece = len(levels[-1]) * max_width
        extra_line = f"{back}{grey}{' ' * (per_piece + padding)}{reset}"
        strings: list[str] = [extra_line]
        for level in levels:
            # printing the data first
            data_string = f'{back}{grey}'
            for node in level:
                data = ''
                if node:
                    data = _mangled(node.data)
                    data = _format(node.color, data)
                data = _node_builder(data, per_piece)
                data_string += data
            per_piece //= 2
            data_string += f"    {reset}"

            # printing the piece
            piece_string = f'{back}{grey}'
            per_node = per_piece // 2
            for node in level:
                piece = ' ' * max_width
                if node:
                    if node.left and node.right:
                        piece = (
                            f"┌{'─' * (per_node - 1)}┴{'─' * (per_node - 1)}┐"
                        )
                    elif node.left:
                        piece = (
                            f" ┌{'─' * (per_node - 1)}┘{' ' * (per_node + 1)}"
                        )
                    elif node.right:
                        piece = (
                            f"{' ' * (per_node + 1)}└{'─' * (per_node - 1)}┐"
                        )
                piece = _node_builder(piece, per_piece * 2, len(piece))
                piece_string += piece

            piece_string += f"    {reset}"
            strings += [data_string, piece_string]
        return '\n'.join(strings)

    # Pre Order Traversal of Tree
    def preorder_print(self) -> None:
        def string_builder(parent: Optional[RedBlackNode],
                           has_right_child: bool,
                           padding="", component="") -> None:
            if not parent:
                return
            data = f'{back}{grey}'
            padding += f'{back}{grey}'
            if self._string is not None:
                data += _format(parent.color, _mangled(parent.data))
                data += f"  {reset}"
                self._string += f"\n{padding}{component}{_mangled(data)}"
            if parent is not root:
                padding += "│   " if has_right_child else "    "
            left_pointer = "├─▶ " if parent.right else "└─▶ "
            right_pointer = "└─▶ "
            string_builder(parent.left, bool(parent.right), padding,
                           left_pointer)
            string_builder(parent.right, False, padding, right_pointer)

        root = self.root
        if not root:
            self._string = "NULL"
            print("NULL")
            return
        self._string = ""
        string_builder(root, bool(root.right))
        print(self._string)
