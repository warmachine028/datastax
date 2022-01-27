from __future__ import annotations

import math
from typing import Any, Optional

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


class HuffmanTree(BinaryTree):
    def insert(self, item: Any):
        raise NotImplementedError

    # Level order Traversal of Tree
    def __str__(self, root=None):  # noqa: C901
        root = root or self.root
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
