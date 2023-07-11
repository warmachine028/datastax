# Private module to separate print logic from main logic of BinaryTree
from __future__ import annotations

import math
from typing import Any, Optional

from datastax.Lists import Queue


def _node_builder(data: Optional[str], piece_width: int) -> str:
    value: str = data or ''
    gap1 = int(math.ceil(piece_width / 2 - len(value) / 2))
    gap2 = int(math.floor(piece_width / 2 - len(value) / 2))
    return f"{' ' * gap1}{value}{' ' * gap2}"


# private method to mangle string __repr__
def _mangled(item: Any) -> str:
    if '\n' in str(item):
        return f"{str(type(item))[8:-2].split('.')[-1]}@{id(item)}"
    return str(item)


class TreeNode:
    def __init__(self, data: Any,
                 left=None,
                 right=None) -> None:
        self.left = left
        self.data = data
        self.right = right

    def __str__(self):
        values = [self.data,
                  self.left.data if self.left else None,
                  self.right.data if self.right else None]
        values = list(
            map(lambda value: "" if value is None else _mangled(value), values)
        )
        max_width = max(len(_mangled(data)) for data in values if data)
        if max_width % 2:
            max_width += 1  # To make max_width even

        "Building string from calculated values"
        per_piece = 2 * (max_width + 4)
        string_builder = f"{_node_builder(values[0], per_piece)}\n"
        per_piece //= 2
        hpw = int(per_piece // 2 - 1)
        if any(values[1:]):
            if all(values[1:]):
                string_builder += (
                    f"{' ' * (hpw + 1)}"
                    f"┌{'─' * hpw}┴{'─' * hpw}┐\n"
                )
                string_builder += _node_builder(
                    values[1], per_piece
                ) + _node_builder(values[2], per_piece)
            elif values[1]:
                string_builder += f"{' ' * (hpw + 1)}┌{'─' * hpw}┘\n"
                string_builder += _node_builder(values[1], per_piece)
            else:
                string_builder += f"{' ' * (per_piece - 1)} └{'─' * hpw}┐\n"
                string_builder += (
                    f"{' ' * (per_piece - 1)} "
                    f"{_node_builder(values[2], per_piece)}"
                )

        return string_builder

    def preorder_print(self) -> str:
        values = [self.data, self.left.data if self.left else None,
                  self.right.data if self.right else None]
        values = list(
            map(lambda value: "" if value is None else _mangled(value), values)
        )

        string_builder = f'{values[0]}\n'
        if any(values[1:]):
            if all(values[1:]):
                string_builder += f"├─▶ {values[1]}\n"
                string_builder += f"└─▶ {values[2]}"
            else:
                string_builder += f"└─▶ {values[1] or values[2]}"

        return string_builder

    def __repr__(self):
        return self.__str__()


class BinaryTree:
    def __init__(self, array=None, root=None):
        self._root = root
        self._construct(array)
        self._string: Optional[str] = None

    @property
    def root(self):
        return self._root

    def _construct(self, array=None):
        if not array or array[0] is None:
            return None
        for item in array:
            try:
                self.insert(item)
            except TypeError as error:
                raise error
        return self

    def insert(self, item: Any):
        raise NotImplementedError

    @property  # Level Order Traversal -> Tree to array
    def array_repr(self) -> list[Any]:
        array = []
        queue = Queue()
        if self.root:
            queue.enqueue(self.root)
        while not queue.is_empty():
            node = queue.dequeue()
            array.append(node.data)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return array

    # Level order Traversal of Tree
    def __str__(self):  # noqa: C901
        root = self.root
        if not root:
            return "  NULL"

        lines: list[list[Optional[str]]] = []
        level: list[Optional[TreeNode]] = [root]
        nodes: int = 1
        max_width: int = 0
        while nodes:
            line: list[Optional[str]] = []
            next_level: list[Optional[TreeNode]] = []
            nodes = 0
            for node in level:
                if node:
                    data = _mangled(node.data)
                    max_width = max(len(data), max_width)
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
    def preorder_print(self) -> None:
        def string_builder(parent: Optional[TreeNode], has_right_child: bool,
                           padding="", component="") -> None:
            if not parent:
                return
            if self._string is not None:
                self._string += (
                    f"\n{padding}{component}"
                    f"{_mangled(parent.data)}"
                )
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
            print(self._string)
            return
        self._string = ""
        string_builder(root, bool(root.right))
        print(self._string)

    def __repr__(self):
        return self.__str__()
