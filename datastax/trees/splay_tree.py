# Splay Tree Implementation
from __future__ import annotations

import warnings
from typing import Any, Optional

from datastax.errors import (
    DuplicateNodeWarning
)
from datastax.trees.binary_search_tree import BinarySearchTree, TreeNode


class SplayNode(TreeNode):
    def __init__(self, data: Any,
                 left: SplayNode = None,
                 right: SplayNode = None) -> None:
        super().__init__(data, left, right)
        self.parent: Optional[SplayNode] = None


class SplayTree(BinarySearchTree):
    # Private helper function for inserting
    def _place(self, parent: Optional[SplayNode], data) -> Optional[SplayNode]:
        node = SplayNode(data)
        parent = None
        search = self.root
        while search:
            parent = search
            if data < search.data:
                search = search.left
            elif search.data < data:
                search = search.right
            else:
                warnings.warn(
                    f"Insertion unsuccessful. Item '{data}' already exists "
                    "in Tree", DuplicateNodeWarning
                )
                return None
        node.parent = parent
        # Node to be added is root node
        if not parent:
            return node
        if parent.data > node.data:
            parent.left = node
        else:
            parent.right = node
        self.splay(node)
        return self.root

    def search(self, data: Any):
        node = super().search(data)
        if node:
            self.splay(node)
        return node

    def _left_rotate(self, node: SplayNode) -> Optional[SplayNode]:
        right = node.right
        if not right:
            return right
        node.right = right.left
        if right.left:
            right.left.parent = node

        right.parent = node.parent
        if node.parent:
            if node is node.parent.left:
                node.parent.left = right
            else:
                node.parent.right = right
        else:
            self._root = right
        right.left = node
        node.parent = right
        return right

    def _right_rotate(self, node: SplayNode):
        left = node.left
        if not left:
            return left
        node.left = left.right
        if left.right:
            left.right.parent = node

        left.parent = node.parent
        if not node.parent:
            self._root = left
        elif node is node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left

        left.right = node
        node.parent = left
        return left

    def delete(self, data: Any = None) -> None:
        super().delete(data)

    def _delete(self, root, item: Any):
        node = super().search(item)
        self.splay(node)

        # Splitting the tree
        # First completing leftSubTree
        left_tree = SplayTree(None, self.root.left)
        if left_tree.root:
            left_tree.root.parent = None

        right_tree = SplayTree(None, self.root.right)
        if right_tree.root:
            right_tree.root.parent = None

        if left_tree.root:
            # Finding the maximum element in left sub tree
            maximum = left_tree.root
            while maximum.right:
                maximum = maximum.right
            left_tree.splay(maximum)
            left_tree.root.right = right_tree.root
            self._root = left_tree.root
        else:
            self._root = right_tree.root
        return self.root

    def splay(self, node: SplayNode) -> Any:
        while node.parent:
            parent = node.parent
            ancestor = parent.parent
            # Parent is root node
            if not ancestor:
                if node is parent.left:
                    self._right_rotate(parent)
                else:
                    self._left_rotate(parent)
                continue

            # RR Rotation: Both are left children
            if parent.left is node and ancestor.left is parent:
                self._right_rotate(ancestor)
                self._right_rotate(parent)
            # LL Rotation: Both are right children
            elif parent.right is node and ancestor.right is parent:
                self._left_rotate(ancestor)
                self._left_rotate(parent)
            # LR Rotation: node is right and parent is left child
            elif parent.right is node and ancestor.left is parent:
                self._left_rotate(parent)
                self._right_rotate(ancestor)
            # RL Rotation: node is left and parent is right child
            elif parent.left is node and ancestor.right is parent:
                self._right_rotate(parent)
                self._left_rotate(ancestor)
