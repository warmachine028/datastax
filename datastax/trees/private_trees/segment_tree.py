from __future__ import annotations

import math
from typing import Any, Optional

from datastax.trees.private_trees.binary_tree import (
    BinaryTree, TreeNode, _node_builder, _mangled
)


class SegmentNode(TreeNode):
    def __init__(self, data: Any,
                 left: SegmentNode = None,
                 right: SegmentNode = None):
        self.left_index = 0
        self.right_index = 0
        super().__init__(data, left, right)


class SegmentTree(BinaryTree):
    def insert(self, item: Any):
        raise NotImplementedError

    @property
    def segment_array(self):
        segment_array = []
        self._traverse_leafs(self.root, segment_array)
        return segment_array

    def _traverse_leafs(self, node, array):
        if not node:
            return
        if not any((node.left, node.right)):
            array.append(node.data)
            return
        # if left child is found, check for leaf node recursively
        if node.left:
            self._traverse_leafs(node.left, array)
        # if right child is found, check for leaf node recursively
        if node.right:
            self._traverse_leafs(node.right, array)

    def __str__(self):  # noqa: C901
        root = self.root
        if not root:
            return "  NULL"

        lines: list[list] = []
        level: list[Optional[SegmentNode]] = [root]
        nodes: int = 1
        max_width: int = 0
        while nodes:
            line: list[Optional[list]] = []
            next_level: list[Optional[SegmentNode]] = []
            nodes = 0
            for node in level:
                if node:
                    data = _mangled(node.data)
                    _range = None
                    if node.left_index != node.right_index:
                        _range = f"[{node.left_index}:{node.right_index}]"
                    max_width = max(len(data), max_width)
                    line.append([data, _range])
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
        string_builder += f"{_node_builder(lines[0][0][1], per_piece)}\n"
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
                value = value[1] if value else value
                string_builder += _node_builder(value, per_piece)
            string_builder += '\n'

            per_piece //= 2

        return string_builder

    def preorder_print(self) -> None:
        def string_builder(parent: Optional[SegmentNode],
                           has_right_child: bool,
                           padding="", component="") -> None:
            if not parent:
                return
            if self._string is not None:
                self._string += (
                    f"\n{padding}{component}"
                    f"{_mangled(parent.data)} "
                )
                if parent.left_index != parent.right_index:
                    self._string += (
                        f"[{parent.left_index}:{parent.right_index}]"
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
            print("NULL")
            return
        self._string = ""
        string_builder(root, bool(root.right))
        print(self._string)
