import warnings
from typing import Any, Optional
from datastax.Utils.Warnings import DuplicateNodeWarning
from datastax.Trees.BinarySearchTree import BinarySearchTree
from datastax.Nodes import AVLNode


class AVLTree(BinarySearchTree):
    def __init__(self, items: Optional[list] = None,
                 root: Optional[AVLNode] = None):
        self.set_root(root)
        super().__init__(items, root)

    # Private helper method for insert function
    def _place(self, parent: AVLNode | None, data) -> AVLNode | None:
        if not parent:
            return AVLNode(data)
        if parent.data < data:
            parent.set_right(self._place(parent.right, data))
        elif data < parent.data:
            parent.set_left(self._place(parent.left, data))
        else:
            warnings.warn(
                f"Insertion unsuccessful. Item '{data}' already exists "
                "in AVLTree", DuplicateNodeWarning
            )
        parent.set_height(1 + max(
            self.height(parent.left),
            self.height(parent.right)
        ))
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
    def height(node: AVLNode | None) -> int:
        return node.height if node else 0

    # Function to balance a node
    def _balance(self, parent: AVLNode | None) -> AVLNode | None:
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
                    parent.set_right(self._right_rotate(parent.right))
                return self._left_rotate(parent)

        if balance_factor > 1:
            # Perform RR Rotation
            # if parent.left and data < parent.left.data:
            if parent.left and self.balance_factor(parent.left) >= 0:
                return self._right_rotate(parent)
            # Perform LR Rotation
            else:
                if parent.left:
                    parent.set_left(self._left_rotate(parent.left))
                return self._right_rotate(parent)
        return parent

    # Private helper method of balance function to perform RR rotation
    def _right_rotate(self, node: AVLNode) -> AVLNode | None:
        left = node.left
        if left:
            temp = left.right
            left.set_right(node)
            node.set_left(temp)
            node.set_height(1 + max(self.height(node.left),
                                    self.height(node.right)))
            left.set_height(1 + max(self.height(left.left),
                                    self.height(left.right)))
        return left

    # Private helper method of balance function to perform LL rotation
    def _left_rotate(self, node: AVLNode) -> AVLNode | None:
        right = node.right
        if right:
            temp = right.left
            right.set_left(node)
            node.set_right(temp)
            node.set_height(1 + max(self.height(node.left),
                                    self.height(node.right)))
            right.set_height(1 + max(self.height(right.left),
                                     self.height(right.right)))
        return right

    def _delete(self, root: AVLNode | None, item: Any) -> AVLNode | None:
        root = super()._delete(root, item)
        if root:
            root.set_height(1 + max(
                self.height(root.left),
                self.height(root.right)
            ))
        return self._balance(root)
