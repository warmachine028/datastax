# AVL Tree Implementation (Also: Self Balancing Binary Tree)
from __future__ import annotations

import warnings
from typing import Any, Optional

from datastax.errors import DuplicateNodeWarning
from datastax.trees.binary_search_tree import BinarySearchTree, TreeNode


class AVLNode(TreeNode):
    def __init__(self, data: Any,
                 left: AVLNode = None,
                 right: AVLNode = None):
        super().__init__(data, left, right)
        self.height = 1


class AVLTree(BinarySearchTree):
    def __init__(self, array: list[Any] = None, root=None):
        self._root: Optional[AVLNode] = root
        super().__init__(array, root)

    # Private helper method for insert function
    def _place(self, parent: Optional[AVLNode], data) -> Optional[AVLNode]:
        if not parent:
            return AVLNode(data)
        if parent.data < data:
            parent.right = self._place(parent.right, data)
        elif data < parent.data:
            parent.left = self._place(parent.left, data)
        else:
            warnings.warn(
                f"Insertion unsuccessful. Item '{data}' already exists "
                "in AVLTree", DuplicateNodeWarning
            )
        parent.height = 1 + max(
            self.height(parent.left),
            self.height(parent.right)
        )
        # Balancing the tree
        return self._balance(parent)

    # Function to check balance factor of node
    def balance_factor(self, parent: Optional[AVLNode] = None) -> int:
        parent = parent or self.root
        if parent:
            return self.height(parent.left) - self.height(parent.right)
        return 0

    # Function to get height of a tree
    @staticmethod
    def height(node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    # Function to balance a node
    def _balance(self, parent: Optional[AVLNode]) -> Optional[AVLNode]:
        if not parent:
            return None
        balance_factor = self.balance_factor(parent)
        if balance_factor < -1:
            # Perform LL Rotation
            # if parent.right and parent.right.data < data:
            if parent.right and self.balance_factor(parent.right) <= 0:
                return self._left_rotate(parent)
            # Perform RL Rotation
            else:
                if parent.right:
                    parent.right = self._right_rotate(parent.right)
                return self._left_rotate(parent)

        if balance_factor > 1:
            # Perform RR Rotation
            # if parent.left and data < parent.left.data:
            if parent.left and self.balance_factor(parent.left) >= 0:
                return self._right_rotate(parent)
            # Perform LR Rotation
            else:
                if parent.left:
                    parent.left = self._left_rotate(parent.left)
                return self._right_rotate(parent)
        return parent

    # Private helper method of balance function to perform RR rotation
    def _right_rotate(self, node: AVLNode) -> Optional[AVLNode]:
        left = node.left
        if left:
            temp = left.right
            left.right = node
            node.left = temp
            node.height = 1 + max(self.height(node.left),
                                  self.height(node.right))
            left.height = 1 + max(self.height(left.left),
                                  self.height(left.right))
        return left

    # Private helper method of balance function to perform LL rotation
    def _left_rotate(self, node: AVLNode) -> Optional[AVLNode]:
        right = node.right
        if right:
            temp = right.left
            right.left = node
            node.right = temp
            node.height = 1 + max(self.height(node.left),
                                  self.height(node.right))
            right.height = 1 + max(self.height(right.left),
                                   self.height(right.right))
        return right

    def _delete(self, root: Optional[AVLNode], item: Any) -> Optional[AVLNode]:
        root = super()._delete(root, item)
        if root:
            root.height = 1 + max(
                self.height(root.left),
                self.height(root.right)
            )
        return self._balance(root)
