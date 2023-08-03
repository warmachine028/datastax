import math
from typing import Any, Optional
from datastax.Nodes import TreeNode
from datastax.Lists import Queue
from datastax.Utils import Commons
from abc import ABC as AbstractClass, abstractmethod


class BinaryTree(AbstractClass):
    _root: Optional[TreeNode]
    _string: Optional[str]

    @property
    def root(self):
        return self._root

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
    def __str__(self):
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

        string_builder = f"{Commons.node_builder(lines[0][0], per_piece)}\n"
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
                string_builder += Commons.node_builder(value, per_piece)
            string_builder += "\n"
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
                    f"\n{padding}{component}" f"{Commons.repr(parent.data)}"
                )
            if parent is not root:
                padding += "│   " if has_right_child else "    "
            left_pointer = "├─▶ " if parent.right else "└─▶ "
            right_pointer = "└─▶ "
            string_builder(
                parent.left, bool(parent.right), padding, left_pointer
            )
            string_builder(parent.right, False, padding, right_pointer)

        root = self.root
        if not root:
            self._string = "NULL"
            print(self._string)
            return
        self._string = ""
        string_builder(root, bool(root.right))
        print(self._string)

    @abstractmethod
    def insert(self, item: Any):
        ...

    @abstractmethod
    def set_root(self, root: TreeNode):
        ...
