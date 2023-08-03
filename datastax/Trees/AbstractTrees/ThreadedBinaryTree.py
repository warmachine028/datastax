from itertools import chain
from typing import Optional, Any
from abc import ABC as AbstractClass, abstractmethod
from datastax.Utils import Commons
from datastax.Trees.AbstractTrees.BinaryTree import BinaryTree
from datastax.Nodes import ThreadedNode


class ThreadedBinaryTree(BinaryTree, AbstractClass):

    # Level order Traversal of Tree
    def __str__(self):  # noqa: C901
        root = self.root
        if not root:
            return "  NULL"
        levels = self._nodes_level_wise(root)  # get all the levels
        max_width = self._maximum_width(levels)  # get the maximum_with of data
        padding = 6
        per_piece = len(levels[-1]) * (max_width + padding) * 2
        strings = []
        for level in levels:
            # Constructing the data line
            data_string = ""
            for node in level:
                data = Commons.repr(node.data) if node else ''
                data = data.center(per_piece)
                data_string += data

            # Constructing the part line below data line '┌└┴┘┐'
            part_string = ""
            wpn = per_piece // 2 - 1
            wpn = (wpn + 1) if wpn % 2 else wpn
            for node in level:
                if node:
                    piece = '┴'.center(wpn, '─')
                    piece = f"{'┌' if node.left_is_child else '└'}{piece[:-1]}"
                    piece = f"{piece}{'┐' if node.right_is_child else '┘'}"
                    data = piece.center(per_piece)
                else:
                    data = ' '.center(per_piece)
                part_string += data
            strings.append(data_string)
            strings.append(part_string)
            per_piece //= 2

        self._draw_threads(strings)  # draws the threads
        self._draw_header(strings)  # draws the header

        return '\n'.join(string.rstrip() for string in strings)

    def preorder_print(self) -> None:
        def string_builder(parent: Optional[ThreadedNode],
                           has_right_child: bool,
                           padding="", component="") -> None:
            if not parent:
                return
            if self._string is not None:
                self._string += (
                    f"\n{padding}{component}"
                    f"{Commons.repr(parent.data)}"
                )
            if parent is not root:
                padding += "│   " if has_right_child else "    "
            left_pointer = "├─▶ " if parent.right_is_child else "└─▶ "
            right_pointer = '└─▶ '
            string_builder(parent.left if parent.left_is_child else None,
                           parent.right_is_child, padding, left_pointer)
            string_builder(parent.right if parent.right_is_child else None,
                           False, padding, right_pointer)

        root = self.root
        if not root:
            self._string = "NULL"
            print(self._string)
            return
        self._string = ''
        string_builder(root, root.right_is_child)
        print(self._string)

    # private helper methods for __str__() method
    @staticmethod
    def _nodes_level_wise(root: ThreadedNode) -> list[list]:
        level: list = [root]
        nodes: int = 1
        levels: list[list] = []
        while nodes:
            current_level: list[Optional[ThreadedNode]] = []
            next_level = []
            nodes = 0
            for node in level:
                if not node:
                    current_level.append(None)
                    next_level += [None] * 2
                    continue
                current_level.append(node)
                next_level += [
                    node.left if node.left_is_child else None,
                    node.right if node.right_is_child else None
                ]
                if node.left_is_child:
                    nodes += 1
                if node.right_is_child:
                    nodes += 1

            levels.append(current_level)
            level = next_level
        return levels

    @staticmethod
    def _maximum_width(levels: list[list]) -> int:
        data = [
            Commons.repr(node.data) for node in filter(bool, chain(*levels))
        ]
        max_width = max(map(len, data))
        return max_width + 1 if max_width % 2 else max_width

    @staticmethod
    def _draw_threads(strings: list[str]) -> None:
        def replace(str_no, char_no):
            for i in range(str_no, -1, -1):
                line = strings[i]
                if line[char_no] != ' ':
                    return
                strings[i] = f"{line[:char_no]}│{line[char_no + 1:]}"

        for s, string in enumerate(strings):
            for c, char in enumerate(string):
                if char in ('└', '┘'):
                    replace(s - 1, c)

    def _draw_header(self, strings: list[str]) -> None:
        first, last = strings[0].find('│'), strings[0].rfind('│')
        root = str(self.root.data)
        first_item_index = strings[0].find(root) + len(root) // 2 - 1

        top = '    ┌───┐'
        dummy_node = '> DUMMY │<'
        part = '┌───┴───┘'
        starting_position = first_item_index - first

        # Shrink that part
        if last - first < len(dummy_node) + starting_position:
            top = '    ┌┐'
            dummy_node = '>DU..│<'
            part = '   ┌┴┘'
            starting_position -= len(dummy_node) // 2 + bool(not len(root) % 2)

        top = f"\n {' ' * first}{' ' * starting_position}{top}"
        middle = f"{' ' * first}┌{'─' * starting_position}{dummy_node}"
        bottom = f"{' ' * first}│{' ' * starting_position}{part}"
        middle += f"{'─' * (last - len(middle))}┐"
        bottom += f"{' ' * (last - len(bottom))}│"
        for string in [bottom, middle, top]:
            strings.insert(0, string)

    @abstractmethod
    def inorder(self) -> list[Any]:
        ...

    @abstractmethod
    def convert_from(self, root) -> None:
        ...
