import warnings
from typing import Any, Optional

from datastax.Utils.Warnings import (
    DuplicateNodeWarning,
    DeletionFromEmptyTreeWarning,
    NodeNotFoundWarning
)

from datastax.Trees.BinarySearchTree import BinarySearchTree
from datastax.Nodes import SplayNode


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
                    "in Tree. Splaying it",
                    DuplicateNodeWarning
                )
                if parent:
                    self._splay(parent)
                return None
        node.set_parent(parent)
        # Node to be added is root node
        if not parent:
            return node
        if parent.data > node.data:
            parent.set_left(node)
        else:
            parent.set_right(node)
        self._splay(node)
        return self.root

    def search(self, data: Any):
        """
        Searches a node in log2(n) time complexity BinarySearch Algorithm
        :param data: Any type of content in BST to search
        :return: SplayNode if it is found else None
        """
        if data is None:
            return None

        root = self.root
        parent = node = None
        while root:
            parent = root
            if root.data == data:
                node = root
                break
            elif root.data < data:
                root = root.right
            else:
                root = root.left

        if node:
            self._splay(node)
        elif parent:
            warnings.warn(
                f"Node was not found with current data '{data}'. "
                f"Splaying last accessed Node '{parent.data}'",
                NodeNotFoundWarning
            )
            self._splay(parent)
        else:
            warnings.warn(
                f"Node was not found with current data '{data}'. "
                f"Tree is empty", NodeNotFoundWarning
            )
        return self.root

    # Private helper method of balance function to perform RR rotation
    def _zig_rotate(self, node: SplayNode) -> Optional[SplayNode]:
        left = node.left
        if not left:
            return left
        left.set_parent(node.parent)

        node.set_left(left.right)
        if node.left:
            node.left.set_parent(node)
        left.set_right(node)
        node.set_parent(left)

        if left.parent:
            if node is left.parent.left:
                left.parent.set_left(left)
            else:
                left.parent.set_right(left)
        else:
            self.set_root(left)
        return left

    # Private helper method of balance function to perform LL rotation
    def _zag_rotate(self, node: SplayNode) -> Optional[SplayNode]:
        right = node.right
        if not right:
            return right
        right.set_parent(node.parent)

        node.set_right(right.left)
        if node.right:
            node.right.set_parent(node)

        right.set_left(node)
        node.set_parent(right)

        if right.parent:
            if node is right.parent.left:
                right.parent.set_left(right)
            else:
                right.parent.set_right(right)
        else:
            self.set_root(right)
        return right

    def delete(self, data: Any = None) -> None:
        if not self.root:
            warnings.warn(
                "Deletion Unsuccessful. Can't delete from empty Tree",
                DeletionFromEmptyTreeWarning
            )
            return
        self.set_root(self._delete(self.root, data))

    def _delete(self, root, item: Any):
        node = self.search(item)

        if node.data != item:  # item was not found
            return self.root
        # Splitting the tree
        # First completing leftSubTree
        left_tree = SplayTree(None, self.root.left)
        if left_tree.root:
            left_tree.root.set_parent(None)

        right_tree = SplayTree(None, self.root.right)
        if right_tree.root:
            right_tree.root.set_parent(None)

        if left_tree.root:
            # Finding the maximum element in left subtree
            predecessor = self.inorder_predecessor(self.root)
            if predecessor:
                left_tree._splay(predecessor)
            left_tree.root.set_right(right_tree.root)
            if right_tree.root:
                right_tree.root.set_parent(left_tree.root)
            self._root = left_tree.root
        else:
            self._root = right_tree.root

        return self.root

    def _splay(self, node: SplayNode):
        """
        Private function that accepts a node and pulls it up to the root
        :param node: A node to be splayed
        :return: Nothing
        """
        while node.parent:
            parent = node.parent
            ancestor = parent.parent
            # Parent is root node
            if not ancestor:
                # directly perform zig or zag rotation
                if node is parent.left:
                    self._zig_rotate(parent)  # zig rotation
                else:
                    self._zag_rotate(parent)  # zag rotation
                continue

            # RR Rotation: Both are left children
            if parent.left is node and ancestor.left is parent:
                self._zig_rotate(ancestor)
                self._zig_rotate(parent)
            # LL Rotation: Both are right children
            elif parent.right is node and ancestor.right is parent:
                self._zag_rotate(ancestor)
                self._zag_rotate(parent)
            # LR Rotation: node is right and parent is left child
            elif parent.right is node and ancestor.left is parent:
                self._zag_rotate(parent)
                self._zig_rotate(ancestor)
            # RL Rotation: node is left and parent is right child
            else:
                self._zig_rotate(parent)
                self._zag_rotate(ancestor)
