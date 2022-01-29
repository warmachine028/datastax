from __future__ import annotations

import math
from typing import Any, Optional

from datastax.trees.private_trees.binary_tree import (
    TreeNode,
    BinaryTree,
    _mangled,
)

RED = 0
BLACK = 1


def _node_builder(data: Optional[str], piece_width: int) -> str:
    value: str = data or ''
    n = len(value) - 27 if value else 0
    gap1 = int(math.ceil(piece_width / 2 - n / 2))
    gap2 = int(math.floor(piece_width / 2 - n / 2))
    return f"{' ' * gap1}{value}{' ' * gap2}"


class RedBlackNode(TreeNode):

    def __init__(self, data: Any,
                 left: RedBlackNode = None,
                 right: RedBlackNode = None,
                 color: int = RED):
        super().__init__(data, left, right)
        self.parent: Optional[RedBlackNode] = None
        self.color = color


class RedBlackTree(BinaryTree):
    def insert(self, item: Any):
        raise NotImplementedError

    @staticmethod
    def _format(color, data):
        black, red = '232m', '196m'
        fore, back = '\x1B[38;5;', '\x1B[48;5;'
        if color == BLACK:
            return f"{fore}{red}{back}{black}  {data}  \x1b[0m"
        return f"{fore}{black}{back}{red}  {data}  \x1b[0m"

    # Level order Traversal of Tree
    def __str__(self):  # noqa: C901
        root = self.root
        if not root:
            return "  NULL"

        lines: list[list[Optional[str]]] = []
        level: list[Optional[RedBlackNode]] = [root]
        nodes: int = 1
        max_width: int = 0
        while nodes:
            line: list[Optional[str]] = []
            next_level: list[Optional[RedBlackNode]] = []
            nodes = 0
            for node in level:
                if node:
                    data = _mangled(node.data)
                    data = self._format(node.color, data)
                    max_width = max(len(data) - 30, max_width)
                    line.append(data)
                    next_level += [node.left, node.right]
                    if node.left:
                        nodes += 1
                    if node.right:
                        nodes += 1
                    continue
                line.append(None)
                next_level += [None] * 2
            if max_width % 2:
                max_width += 1
            lines.append(line)
            level = next_level
        ##################################################################
        "Building string from calculated values"
        per_piece = len(lines[-1]) * (max_width + 4)

        string_builder = f"{_node_builder(lines[0][0], per_piece)}\n"
        per_piece //= 2
        for _, line in enumerate(lines[1:], 1):
            hpw = int(math.floor(per_piece / 2) - 1)
            # Printing ┌ ┴ ┐ or ┌ ─ ┘ or └ ─ ┐ components
            for j, value in enumerate(line):
                string_builder += (
                    ('┴' if value else '┘') if line[j - 1] else (
                        '└' if value else ' ')) if j % 2 else ' '

                if not value:
                    string_builder += ' ' * (per_piece - 1)
                    continue
                if j % 2:
                    string_builder += f"{'─' * hpw}┐{' ' * hpw}"
                else:
                    string_builder += f"{' ' * hpw}┌{'─' * hpw}"
            string_builder += '\n'

            # Printing the value of each Node
            for value in line:
                string_builder += _node_builder(value, per_piece)
            string_builder += '\n'
            per_piece //= 2

        return string_builder

    # Pre Order Traversal of Tree
    def preorder_print(self, root=None) -> str:
        def string_builder(parent: Optional[RedBlackNode],
                           has_right_child: bool,
                           padding="", component="") -> None:
            if not parent:
                return
            if self.__string is not None:
                data = parent.data
                if parent.color == RED:
                    data = "\x1B[48;5;196m\x1B[38;5;232m{}\x1B[0m".format(
                        data)
                self.__string += f"\n{padding}{component}{_mangled(data)}"
            if parent is not root:
                padding += "│   " if has_right_child else "    "
            left_pointer = "├─▶ " if parent.right else "└─▶ "
            right_pointer = "└─▶ "
            string_builder(parent.left, bool(parent.right), padding,
                           left_pointer)
            string_builder(parent.right, False, padding, right_pointer)

        root = root or self.root
        if not root:
            return "NULL"
        self.__string = ""
        string_builder(root, bool(root.right))
        return self.__string
