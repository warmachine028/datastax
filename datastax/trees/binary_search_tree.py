# Binary Search Tree Implementation
from __future__ import annotations

import warnings
from typing import Optional, Any

from datastax.errors import (
    DuplicateNodeWarning,
    DeletionFromEmptyTree,
    NodeNotFoundWarning
)
from datastax.trees.private_trees.binary_tree import BinaryTree, TreeNode


class BinarySearchTree(BinaryTree):

    def insert(self, data: Any) -> None:
        root = self.root
        if data is None:
            return
        result = self._place(root, data)
        if result:
            self._root = result

    def search(self, data: Any):
        """
        Searches a node in log2(n) time complexity BinarySearch Algorithm
        :param data: Any type of content in BST
        :return: TreeNode if it is found else None
        """

        def _search(node):
            if not node:
                return
            if data == node.data:
                return node
            return _search(node.left if data < node.data else node.right)

        if data is None:
            return None
        return _search(self.root)

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
                "in Tree", DuplicateNodeWarning
            )
        return parent

    @staticmethod
    def inorder_predecessor(node):
        node = node.left
        while node.right:
            node = node.right
        return node

    def _delete(self, root, item: Any):
        if not root:
            return None
        if root.data == item:
            # Node with only rightChild, replace with left_child
            if root.left is None:
                return root.right
            # Node with only leftChild, replace with right_child
            if root.right is None:
                return root.left
            # Node with both children, replace with inorder_predecessor
            predecessor = self.inorder_predecessor(root)
            root.data = predecessor.data
            root.left = self._delete(root.left, root.data)
        elif item < root.data:
            root.left = self._delete(root.left, item)
        elif root.data < item:
            root.right = self._delete(root.right, item)
        return root

    def delete(self, data: Any = None) -> None:
        """
        Deletes a node which has the data and replaces with inorder predecessor
        :param data: An item corresponding to the node to be deleted
        :return: returns data if node is found else None and raises warning
        """
        if not self.root:
            warnings.warn(
                "Deletion Unsuccessful. Can't delete from empty Tree",
                DeletionFromEmptyTree
            )
        if not self.search(data):
            warnings.warn(
                "Deletion unsuccessful. Node was not found with current "
                f"data '{data}'", NodeNotFoundWarning
            )
        self._root = self._delete(self.root, data)
