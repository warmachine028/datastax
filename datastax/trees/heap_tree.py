# Heap Tree Implementation
from __future__ import annotations

import warnings
from typing import Optional, Any

from datastax.errors import DeletionFromEmptyTreeWarning
from datastax.trees.private_trees.binary_tree import BinaryTree, TreeNode


class HeapNode(TreeNode):
    def __init__(self, data: Any,
                 left: HeapNode = None,
                 right: HeapNode = None):
        super().__init__(data, left, right)
        self.parent: Optional[HeapNode] = None
        self.prev_leaf: Optional[HeapNode] = None


class HeapTree(BinaryTree):
    def __init__(self, array: list[Any] = None, root: HeapNode = None):
        self._root: Optional[HeapNode] = root
        self._leaf: Optional[HeapNode] = root
        super().__init__(array, root)

    def _construct(self, array: list[Any] = None) -> Optional[HeapTree]:
        if not array or array[0] is None:
            return None
        for item in array:
            try:
                self.heappush(item)
            except TypeError as error:
                raise error
        return self

    @property
    def leaf(self):
        return self._leaf

    # Function to push an element inside a tree
    def heappush(self, data: Any) -> None:
        root = self.root
        if data is None:
            return
        node = HeapNode(data)
        if root is None:  # Heap Tree is Empty
            self._root = self._leaf = node
        # Heap tree has nodes. So inserting new node
        # in the left of leftmost leaf node
        elif self.leaf and self.leaf.left is None:
            self.leaf.left = node
            node.parent = self.leaf
        else:
            if not self.leaf:
                return
            self.leaf.right = node
            previous_leaf = self.leaf
            node.parent = self.leaf
            self._update_leaf(self.leaf)
            self.leaf.prev_leaf = previous_leaf
        self._heapify(node)

    # Private function to convert a subtree to heap
    def _heapify(self, node: HeapNode) -> None:
        if node.parent and node.parent.data < node.data:
            node.parent.data, node.data = node.data, node.parent.data
            self._heapify(node.parent)

    # Private Helper method of heappush function to
    # update rightmost node in deepest level
    def _update_leaf(self, node: HeapNode) -> None:
        # reach extreme left of next level if current level is full
        if node.parent is None:
            self._leaf = node
        elif node.parent.left is node:
            self._leaf = node.parent.right
        elif node.parent.right is node:
            self._update_leaf(node.parent)
        while self.leaf and self.leaf.left:
            self._leaf = self.leaf.left

    # Function to pop the largest element in the tree
    def heappop(self) -> Optional[Any]:
        if not self.root:
            warnings.warn(
                "Deletion Unsuccessful. Can't delete when"
                "tree is Already Empty", DeletionFromEmptyTreeWarning
            )
            return None
        deleted_data = self.root.data
        if self.root is self.leaf and not any(
                [self.leaf.left, self.leaf.right]):
            self._root = self._leaf = None

        else:
            if self.leaf.right and self.root:
                self.root.data = self.leaf.right.data
                self.leaf.right = None
                self._shift_up(self.root)
            elif self.leaf.left and self.root:
                self.root.data = self.leaf.left.data
                self.leaf.left = None
                self._shift_up(self.root)
            else:  # We have reached the end of a level
                self._leaf = self.leaf.prev_leaf
                return self.heappop()
        return deleted_data

    # Private helper method of heappop function
    def _shift_up(self, node: HeapNode) -> None:
        root = node
        left_child = root.left
        right_child = root.right
        if left_child and left_child.data > root.data:
            root = left_child
        if right_child and right_child.data > root.data:
            root = right_child
        if root is node:
            return
        root.data, node.data = node.data, root.data
        self._shift_up(root)

    def insert(self, item: Any):
        self.heappush(item)
