# Binary Tree Implementation
from __future__ import annotations

import warnings
from queue import Queue
from typing import Any, Optional

from datastax.errors import (
    PathNotGivenError,
    PathNotFoundError,
    PathAlreadyOccupiedWarning
)
from datastax.trees.private_trees import binary_tree
from datastax.trees.private_trees.binary_tree import TreeNode


class BinaryTree(binary_tree.BinaryTree):
    def insert_path(self, data: Any, path: list[str] = None) -> None:
        node = TreeNode(data)
        if not self._root:
            self._root = node
            return
        if not path:
            raise PathNotGivenError(self)
        parent = self._root
        for direction in path[:-1]:  # Reaching
            if direction == 'left' and parent.left:
                parent = parent.left
            elif direction == 'right' and parent.right:
                parent = parent.right
            else:
                raise PathNotFoundError(self)
        if path[-1] == 'right' and not parent.right:
            parent.right = node
        elif path[-1] == 'left' and not parent.left:
            parent.left = node
        else:
            occupied_node = parent.left if path[-1] == 'left' else parent.right
            warnings.warn("Insertion unsuccessful. Path already occupied by "
                          f"TreeNode [{occupied_node.data}]",
                          PathAlreadyOccupiedWarning)

    # Helper function to construct tree by level order -> Array to tree
    def _construct(self, array: list[Any] = None) -> Optional[BinaryTree]:
        if not array or array[0] is None:
            return None

        queue: Queue[TreeNode] = Queue(len(array))
        current = 0
        root = self.root
        if not root:
            root = TreeNode(array[0])
            current = 1
        queue.put(root)
        while not queue.empty() and current < len(array):
            node = queue.get()
            node.left = None if array[current] is None else TreeNode(
                array[current])
            if node.left:
                queue.put(node.left)  # Inserting Left Node
            current += 1

            if current >= len(array):
                break

            node.right = None if array[current] is None else TreeNode(
                array[current])
            if node.right:
                queue.put(node.right)  # Inserting Right Node
            current += 1
        self._root = root
        return self

    def insert(self, item: Any):
        raise NotImplementedError
