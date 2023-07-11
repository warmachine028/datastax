# Private module to separate print logic from insertion logic
from __future__ import annotations

from itertools import chain
from typing import Optional, Any

from datastax.Lists import Queue
from datastax.trees import (
    BinaryTree,
    AVLTree,
    HeapTree,
    MinHeapTree
)
from datastax.trees.private_trees import binary_tree
from datastax.trees.private_trees.binary_tree import TreeNode, _mangled


class ThreadedNode(TreeNode):
    def __init__(self, data: Any,
                 left: ThreadedNode = None,
                 right: ThreadedNode = None) -> None:
        super().__init__(data, left, right)
        self.left_is_child = bool(self.left)
        self.right_is_child = bool(self.right)

    def __str__(self):
        values = [self.data, self.left.data, self.right.data]
        values = list(
            map(lambda value: "" if value is None else _mangled(value), values)
        )
        max_width = max(len(_mangled(data)) for data in values if data)
        max_width = (max_width + 1) if max_width % 2 else max_width
        # To make max_width even
        padding = 6
        per_piece = (max_width + padding) * 2
        # Building the part first
        wpn = per_piece // 2 - 1
        wpn = (wpn + 1) if wpn % 2 else wpn
        piece = '┴'.center(wpn, '─')
        piece = f"{'┌' if self.left_is_child else '└'}{piece[:-1]}"
        piece = f"{piece}{'┐' if self.right_is_child else '┘'}"
        piece = piece.center(per_piece) + '\n'

        root = values[0]
        left = values[1].center(wpn)
        right = f"{values[2].center(wpn)}\n"
        if self.left_is_child:
            if self.right_is_child:
                _string = (
                        f"{root.center(wpn - 1)}".center(per_piece) +
                        f"\n{piece}{left}{right}"
                )
            else:
                _string = (
                        f"{' ' * len(left)}{right}"
                        f"{root.center(wpn)}│".center(per_piece) +
                        f"\n{piece}{left}"
                )
        else:
            _string = left
            if self.right_is_child:
                _string += (
                        f"\n│{root.center(wpn)}".center(per_piece) +
                        f"\n{piece}{' ' * len(left)}{right}"
                )
            else:
                _string += (
                        f"{right}"
                        f"│{root.center(wpn - 1)}│".center(per_piece) +
                        f"\n{piece}"
                )
        return _string

    def preorder_print(self) -> str:
        values = [self.data, self.left.data if self.left_is_child else None,
                  self.right.data if self.right_is_child else None]
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


class ThreadedBinaryTree(binary_tree.BinaryTree):
    def __init__(self, array=None, root: ThreadedNode = None, *,
                 insertion_logic: str = None
                 ):
        self._root: Optional[ThreadedNode] = root
        self.head = self.tail = self.root
        self.dummy_node = ThreadedNode(None, self.root)
        self.dummy_node.right = self.dummy_node

        self.tree: Any = self
        if insertion_logic is None or insertion_logic.lower() in (
                'threadedbinarytree', 'binarysearchtree'):
            super().__init__(array, root)
        elif insertion_logic.lower() == "binarytree":
            self.tree = BinaryTree(array)
        elif insertion_logic.lower() == "avltree":
            self.tree = AVLTree(array)
        elif insertion_logic.lower() == "heaptree":
            self.tree = HeapTree(array)
        elif insertion_logic.lower() == "minheaptree":
            self.tree = MinHeapTree(array)
        else:  # else Construct tree using BinarySearchTree Logic
            print("This tree is has no insertion logic.",
                  "Building tree using generic BinarySearchTree Logic")
            super().__init__(array, root)
        if not isinstance(self.tree, ThreadedBinaryTree):
            self.convert_to_tbt(self.tree.root)

    def convert_to_tbt(self, root) -> None:
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
            if node.left_is_child:
                queue.enqueue(node.left)
            if node.right_is_child:
                queue.enqueue(node.right)

        return array

    def insert(self, data: Any, root: ThreadedNode = None) -> None:
        raise NotImplementedError

    # Level order Traversal of Tree
    def __str__(self):  # noqa: C901
        root = self.root
        if not root:
            return "  NULL"
        levels = self._nodes_level_wise(root)  # get all the levels
        max_width = self._maximum_width(levels)  # get the maximum_with of data
        padding = 6
        per_piece = len(levels[-1]) * (max_width + padding) * 2
        strings: list[str] = []
        for level in levels:
            # Constructing the data line
            data_string = ""
            for node in level:
                data = _mangled(node.data) if node else ''
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
                    f"{_mangled(parent.data)}"
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
        data = [_mangled(node.data) for node in filter(bool, chain(*levels))]
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
