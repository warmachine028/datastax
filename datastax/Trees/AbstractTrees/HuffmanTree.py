import math
from typing import Optional
from abc import ABC as AbstractClass, abstractmethod
from datastax.Utils import Commons
from datastax.Nodes import HuffmanNode
from datastax.Tables import HuffmanTable
from datastax.Trees.AbstractTrees.BinaryTree import BinaryTree


class HuffmanTree(BinaryTree, AbstractClass):
    _data: Optional[list[str] | str]
    _table: Optional[HuffmanTable] = None
    _huffman_code = ""

    @property
    def huffman_table(self):
        return self._table

    @property
    def huffman_code(self):
        return self._huffman_code

    # Level order Traversal of Tree
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
                    data = Commons.repr(node.data or node.frequency)
                    frequency = "│"
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
        string_builder = f"{Commons.node_builder(lines[0][0][0], per_piece)}\n"
        string_builder += Commons.node_builder("   0", per_piece // 2)
        string_builder = (
            f"{string_builder[:]}" f"{Commons.node_builder(lines[0][0][1], 1)}"
        )
        string_builder += (
                Commons.node_builder("1   ", per_piece // 2 - 1) + "\n"
        )
        per_piece //= 2
        for _, line in enumerate(lines[1:], 1):
            hpw = int(math.floor(per_piece / 2) - 1)
            # Printing ┌ ┴ ┐ or ┌ ─ ┘ or └ ─ ┐ components
            for j, value in enumerate(line):
                string_builder += (
                    (
                        ("┴" if value else "┘")
                        if line[j - 1]
                        else ("└" if value else " ")
                    )
                    if j % 2
                    else " "
                )

                if not value:
                    string_builder += " " * (per_piece - 1)
                    continue
                if j % 2:
                    string_builder += f"{'─' * hpw}┐{' ' * hpw}"
                else:
                    string_builder += f"{' ' * hpw}┌{'─' * hpw}"
            string_builder += "\n"

            # Printing the value of each Node
            for value in line:
                value = value[0] if value else value
                string_builder += Commons.node_builder(value, per_piece)
            string_builder += "\n"
            for value in line:
                internal = value and value[1] == "│"
                if internal:
                    string_builder += (
                        Commons.node_builder("   0", per_piece // 2)
                    )
                data = f"{value[1]}" if value else value
                piece_width = 1 if internal else per_piece
                string_builder = (
                    f"{string_builder[:] if internal else string_builder}"
                    f"{Commons.node_builder(data, piece_width)}"
                )
                if value and value[1] == "│":
                    string_builder += (
                        Commons.node_builder("1   ", per_piece // 2 - 1)
                    )

            string_builder += "\n"
            per_piece //= 2

        return string_builder

    # Pre Order Traversal of Tree
    def preorder_print(self) -> None:
        def string_builder(
                parent: Optional[HuffmanNode],
                has_right_child: bool,
                padding="",
                component="",
        ) -> None:
            if not parent:
                return
            if self._string is not None:
                self._string += f"\n{padding}{component}"
                data = parent.data
                if not data:
                    data = parent.frequency
                    self._string += str(data)
                else:
                    data = Commons.repr(data)
                    self._string += f"{data} [{parent.frequency}]"
            if parent is not root:
                padding += "│   " if has_right_child else "    "
            left_pointer = "├─▶ " if parent.right else "└─▶ "
            right_pointer = "└─▶ "
            string_builder(parent.left, bool(parent.right),
                           padding, left_pointer)
            string_builder(parent.right, False,
                           padding, right_pointer)

        root = self.root
        if not root:
            self._string = "NULL"
            print(self._string)
            return
        self._string = ""
        string_builder(root, bool(root.right))
        print(self._string)

    @abstractmethod
    def huffman_code_of(self, character: str):
        ...

    @abstractmethod
    def size_calculator(self):
        ...

    @abstractmethod
    def compression_ratio(self):
        ...

    @abstractmethod
    def space_saved(self):
        ...

    @staticmethod
    @abstractmethod
    def decode_from_table(huffman_code: str, huffman_table: dict) -> str:
        ...
