# Binary Search Tree Implementation
from __future__ import annotations

import warnings
from typing import Optional, Any

from datastax.errors import DuplicateNodeWarning
from datastax.trees.binary_tree import BinaryTree, TreeNode


class BinarySearchTree(BinaryTree):
    def _construct(self, array: list[Any] = None
                   ) -> Optional[BinarySearchTree]:
        if not array or array[0] is None:
            return None
        for item in array:
            try:
                self.insert(item)
            except TypeError as error:
                raise error
        return self

    def insert(self, data: Any, root=None) -> None:
        root = root or self.root
        if data is None:
            return
        result = self._place(root, data)
        if result and result is not root:
            self._root = result

    def search(self, data: Any, root=None) -> Optional[TreeNode]:
        def _search(node):
            if not node:
                return
            if data == node.data:
                return node
            return _search(node.left if data < node.data else node.right)

        root = root or self.root
        if data is None:
            return None
        return _search(root)

    # Private helper function for inserting
    def _place(self, parent, data) -> Optional[TreeNode]:
        if not parent:
            return TreeNode(data)
        elif parent.data < data:
            parent.right = self._place(parent.right, data)
        elif parent.data > data:
            parent.left = self._place(parent.left, data)
        else:
            warnings.warn(
                f"Insertion unsuccessful. Item '{data}' already exists "
                "in Tree", DuplicateNodeWarning)
        return parent

    def insert_path(self, data: Any, path: list[str] = None) -> None:
        raise NotImplementedError
