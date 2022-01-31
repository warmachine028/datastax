# Private module to separate print logic from main logic of HuffmanTree
from __future__ import annotations

import math
from typing import Any, Optional, Union

from datastax.trees.private_trees.binary_tree import (
    BinaryTree, TreeNode,
    _node_builder, _mangled
)


class HuffmanNode(TreeNode):
    def __init__(self, data: Any,
                 left: HuffmanNode = None,
                 right: HuffmanNode = None,
                 frequency: int = 1):
        self.frequency = frequency
        super().__init__(data, left, right)

    def __str__(self):
        values = [
            self.data or self.frequency,
            self.left.data or self.left.frequency if self.left else None,
            self.right.data or self.right.frequency if self.right else None
        ]
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
        values = [
            self.data or self.frequency,
            self.left.data or self.left.frequency if self.left else None,
            self.right.data or self.right.frequency if self.right else None
        ]
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


class HuffmanTree(BinaryTree):
    def __init__(self, data: Union[list[str], str] = None):
        self._data: Union[list[str], str, None] = data
        self._huffman_code = ''
        self._table = None
        super().__init__(data)

    @property
    def huffman_table(self) -> Optional[HuffmanTable]:
        return self._table

    @property
    def huffman_code(self):
        return self._huffman_code

    # Level order Traversal of Tree
    def __str__(self):  # noqa: C901
        root = self.root
        if not root:
            return "  NULL"

        lines: list[list] = []
        level: list[Optional[HuffmanNode]] = [root]
        nodes: int = 1
        max_width: int = 0
        while nodes:
            line: list[Optional[list]] = []
            next_level: list[Optional[HuffmanNode]] = []
            nodes = 0
            for node in level:
                if node:
                    data = _mangled(node.data or node.frequency)
                    frequency = '│'
                    if not any([node.left, node.right]):
                        frequency = f"{node.frequency}"
                    max_width = max(len(data), max_width)
                    line.append([data, frequency])
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
        string_builder = f"{_node_builder(lines[0][0][0], per_piece)}\n"
        string_builder += _node_builder('   0', per_piece // 2)
        string_builder = (
            f"{string_builder[:]}"
            f"{_node_builder(lines[0][0][1], 1)}"
        )
        string_builder += _node_builder('1   ', per_piece // 2 - 1) + '\n'
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
                value = value[0] if value else value
                string_builder += _node_builder(value, per_piece)
            string_builder += '\n'
            for value in line:
                internal = value and value[1] == '│'
                if internal:
                    string_builder += _node_builder('   0', per_piece // 2)
                data = f"{value[1]}" if value else value
                string_builder = (
                    f"{string_builder[:] if internal else string_builder}"
                    f"{_node_builder(data, 1 if internal else per_piece)}"
                )
                if value and value[1] == '│':
                    string_builder += _node_builder('1   ',
                                                    per_piece // 2 - 1)

            string_builder += '\n'
            per_piece //= 2

        return string_builder

    # Pre Order Traversal of Tree
    def preorder_print(self) -> None:
        def string_builder(parent: Optional[HuffmanNode],
                           has_right_child: bool,
                           padding="", component="") -> None:
            if not parent:
                return
            if self._string is not None:
                self._string += f"\n{padding}{component}"
                data = parent.data
                if not data:
                    data = parent.frequency
                    self._string += str(data)
                else:
                    data = _mangled(data)
                    self._string += f"{data} [{parent.frequency}]"
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

    def insert(self, item: Any):
        raise NotImplementedError


class HuffmanTable:
    def __init__(self, table: dict[str, str],
                 frequencies: dict[str, int]):
        self._huffman_table = table
        self.frequency = frequencies
        self._size = 0
        self._calculate_size()

    @property
    def data(self) -> dict[str, str]:
        return self._huffman_table

    @property
    def size(self):
        return self._size

    def _calculate_size(self):
        raise NotImplementedError

    def __str__(self):
        items = self.data
        padding = 4
        max_width = max(len(code) for *_, code in items.values()) + padding * 2
        if max_width < 10:
            max_width = 12
        mid_width = max_width * 2 - (4 if max_width > 12 else 0)

        h_border = f"╔{'═' * max_width}╤{'═' * mid_width}╤{'═' * max_width}╗\n"
        header = (
            f"║{'Unique'.center(max_width)}"
            f"│{'Occurrence /'.center(mid_width)}│"
            f"{'Huffman'.center(max_width)}║\n"

            f"║{'Characters'.center(max_width)}"
            f"│{'Frequency'.center(mid_width)}│"
            f"{'Code'.center(max_width)}║\n"
        )
        sep = f"╟{'─' * max_width}┼{'─' * mid_width}┼{'─' * max_width}╢\n"
        data_template = "║{}│{}│{}║\n"

        body = ''
        for character, huffman_code in items.items():
            body += sep
            body += data_template.format(character.center(max_width),
                                         str(
                                             self.frequency[character]
                                         ).center(mid_width),
                                         huffman_code.rjust(
                                             max_width - padding).center(
                                             max_width))
        f_border = f"╚{'═' * max_width}╧{'═' * mid_width}╧{'═' * max_width}╝"
        return h_border + header + body + f_border

    def __repr__(self):
        return self.__str__()
