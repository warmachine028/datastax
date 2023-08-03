from itertools import chain
from typing import Optional
from datastax.Nodes import RedBlackNode
from datastax.Utils import Commons, Colors
from datastax.Trees.AbstractTrees.BinaryTree import BinaryTree
from abc import ABC as AbstractClass, abstractmethod

fore, back, reset = Colors.FORE, Colors.BACK, Colors.RESET
red, black, grey = Colors.RED, Colors.BLACK, Colors.GREY


class RedBlackTree(BinaryTree, AbstractClass):

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
            data = Commons.repr(node.data)
            max_width = max(max_width, len(data) + 4)
        return max_width + 1 if max_width % 2 else max_width

    # Level order Traversal of Tree
    def __str__(self):
        root = self.root
        if not root:
            return "  NULL"
        levels = self._nodes_level_wise(root)
        max_width = self._maximum_width(levels) + 1
        padding = 4
        per_piece = len(levels[-1]) * max_width
        extra_line = f"{back}{grey}{' ' * (per_piece + padding)}{reset}"
        strings = [extra_line]
        for level in levels:
            # printing the data first
            data_string = f'{back}{grey}'
            for node in level:
                data = ''
                if node:
                    data = Commons.repr(node.data)
                    data = Commons.format(node.color, data)
                data = Commons.redblack_node_builder(data, per_piece)
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
                piece = Commons.redblack_node_builder(
                    piece, per_piece * 2, len(piece)
                )
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
                data += Commons.format(parent.color, Commons.repr(parent.data))
                data += f"  {reset}"
                self._string += f"\n{padding}{component}{Commons.repr(data)}"
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

    @abstractmethod
    def _left_rotate(self, node: RedBlackNode) -> RedBlackNode:
        ...

    @abstractmethod
    def _right_rotate(self, node: RedBlackNode) -> RedBlackNode:
        ...

    @abstractmethod
    def _resolve_left_black_conflict(self, node: RedBlackNode) -> RedBlackNode:
        ...

    @abstractmethod
    def _resolve_right_black_conflict(self,
                                      node: RedBlackNode) -> RedBlackNode:
        ...
