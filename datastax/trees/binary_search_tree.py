# Binary Search Tree Implementation
from __future__ import annotations

from typing import Optional, Any

from datastax.trees.binary_tree import BinaryTree, TreeNode


class BinarySearchTree(BinaryTree):
    def _construct(self, array: list[Any] = None) -> Optional[BinarySearchTree]:
        if not array or array[0] is None: return None
        for item in array:
            try:
                self.insert(item)
            except TypeError as error:
                print(error)
                break
        return self
    
    def insert(self, data: Any, root=None) -> None:
        def place(parent: Optional[TreeNode]) -> TreeNode:
            if not parent: return TreeNode(data)
            elif parent.data < data: parent.right = place(parent.right)
            elif data < parent.data: parent.left = place(parent.left)
            return parent
        
        root = root or self.root
        result = place(root)
        if not root: self._root = result
