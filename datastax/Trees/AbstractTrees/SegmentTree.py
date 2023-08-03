import math
from typing import Optional
from abc import ABC as AbstractClass, abstractmethod
from datastax.Utils import Commons
from datastax.Nodes import SegmentNode
from datastax.Trees.AbstractTrees.BinaryTree import BinaryTree


class SegmentTree(BinaryTree, AbstractClass):
    _segment_array: Optional[list]

    @property
    def segment_array(self):
        self._segment_array = []
        self._traverse_leafs(self.root)
        return self._segment_array

    def __str__(self):  # noqa: C901
        root = self.root
        if not root:
            return "  NULL"

        lines = []
        level = [root]
        nodes = 1
        max_width = 0
        while nodes:
            line = []
            next_level = []
            nodes = 0
            for node in level:
                if node:
                    data = Commons.repr(node.data)
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

        string_builder = f"{Commons.node_builder(lines[0][0][0], per_piece)}\n"
        string_builder += \
            f"{Commons.node_builder(lines[0][0][1], per_piece)}\n"
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
                string_builder += Commons.node_builder(value, per_piece)
            string_builder += '\n'
            for value in line:
                value = value[1] if value else value
                string_builder += Commons.node_builder(value, per_piece)
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
                    f"{Commons.repr(parent.data)} "
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

    @abstractmethod
    def update_at_range(self, left: int, right: int, data: int) -> None:
        ...

    @abstractmethod
    def update_at_index(self, index: int, data: int) -> None:
        ...

    @abstractmethod
    def get_range(self, left: int, right: int,
                  root: SegmentNode | None,
                  lazy_node: SegmentNode | None):
        ...

    @abstractmethod
    def _traverse_leafs(self, node: SegmentNode | None) -> None:
        ...
