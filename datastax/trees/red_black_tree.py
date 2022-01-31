# Implementation of Variable size Huffman Coding Tree
from __future__ import annotations

import warnings
from typing import Optional, Any

from datastax.errors import (
    DuplicateNodeWarning
)
from datastax.trees.binary_search_tree import BinarySearchTree
from datastax.trees.private_trees import red_black_tree
from datastax.trees.private_trees.red_black_tree import (
    RedBlackNode,
    BLACK, RED
)


class RedBlackTree(BinarySearchTree,
                   red_black_tree.RedBlackTree,
                   ):
    # Private helper function for inserting
    def _place(self,
               parent: Optional[RedBlackNode],
               data) -> Optional[RedBlackNode]:
        node = RedBlackNode(data)
        if self.root is None:
            node.color = BLACK
            return node
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
        if not parent:
            return self.root
        if parent.data > node.data:
            parent.left = node
        else:
            parent.right = node
        self._post_place(node)
        return self.root

    @staticmethod
    def sibling_of(node: Optional[RedBlackNode]):
        if not node or not node.parent:
            return None
        if node.parent.left is node:
            return node.parent.right
        return node.parent.left

    def _post_place(self, node: Optional[RedBlackNode]):
        if not node or node is self.root:
            return
        # ** Resolve Red Red Conflict
        parent = node.parent
        if parent and parent.color == RED:
            sibling = self.sibling_of(parent)
            # CASE 1: Recolor and move up to see if more work required.
            if sibling and sibling.color == RED:
                parent.color = sibling.color = BLACK
                if parent.parent and parent.parent is not self.root:
                    parent.parent.color = RED
                    self._post_place(parent.parent)
            # CASE 2: Color is black so restructuring (rotations) and
            # recoloring both are required.
            else:
                # CASE A: Parent is left child
                if parent.parent and parent is parent.parent.left:
                    # CASE i: Perform RR Rotation
                    # Both node and parent are Left Child of G.Parent
                    if node is parent.right:
                        # CASE ii: Perform LR Rotation
                        # node is Right and parent is Left Child of G.Parent
                        parent = self._left_rotate(parent)
                    if parent and parent.parent:
                        parent.color = BLACK
                        parent.parent.color = RED
                        self._right_rotate(parent.parent)
                # CASE B: Parent is right child
                else:
                    # CASE i: Perform LL Rotation
                    # Both node and parent are Right Child of G.Parent
                    if node is parent.left:
                        # CASE ii: Perform RL Rotation
                        # node is Left and parent is Right Child of G.Parent
                        parent = self._right_rotate(parent)
                    if parent and parent.parent:
                        parent.color = BLACK
                        parent.parent.color = RED
                        self._left_rotate(parent.parent)

    # Private helper method of balance function to perform RR rotation
    def _right_rotate(self, node: RedBlackNode) -> Optional[RedBlackNode]:
        left = node.left
        if not left:
            return left
        left.parent = node.parent

        node.left = left.right
        if node.left:
            node.left.parent = node
        left.right = node
        node.parent = left

        if left.parent:
            if node is left.parent.left:
                left.parent.left = left
            else:
                left.parent.right = left
        else:
            self._root = left
        return left

    # Private helper method of balance function to perform LL rotation
    def _left_rotate(self, node: RedBlackNode) -> Optional[RedBlackNode]:
        right = node.right
        if not right:
            return right
        right.parent = node.parent

        node.right = right.left
        if node.right:
            node.right.parent = node

        right.left = node
        node.parent = right

        if right.parent:
            if node is right.parent.left:
                right.parent.left = right
            else:
                right.parent.right = right
        else:
            self._root = right
        return right

    def _delete(self, root, item: Any):
        node = self.search(item)

        if node and node.left and node.right:
            predecessor = self.inorder_predecessor(node)
            node.data = predecessor.data
            node = predecessor
        if not node:
            return None
        pull_up = node.right if not node.left else node.left
        if pull_up:
            if node is self.root:
                self._root = pull_up
            elif node.parent.left is node:
                node.parent.left = pull_up
            else:
                node.parent.right = pull_up
            if node.color == BLACK:
                self._post_delete(pull_up)
        elif node is self.root:
            self._root = None
        else:
            if node.color == BLACK:
                self._post_delete(node)
            if node.parent.left is node:
                node.parent.left = None
            else:
                node.parent.right = None

        return self.root

    def _post_delete(self, node: Optional[RedBlackNode]):
        # if not node:
        #     return
        # ! Resolve Double Black sentinel Conflict
        while node and node is not self.root and node.color == BLACK:
            parent = node.parent
            if not parent:
                break
            if node is parent.left:
                sibling = parent.right
                if not sibling:
                    break
                # CASE 1: Sibling is RED
                if sibling.color == RED:
                    sibling.color = BLACK
                    parent.color = RED
                    self._left_rotate(parent)
                    sibling = parent.right
                # CASE 2: Sibling is Black
                # CASE A: Both children are also black
                if sibling.left.color == sibling.right.color == BLACK:
                    sibling.color = RED
                    node = parent
                # CASE B: left child is red
                elif sibling.right:
                    # CASE i: right Child Black
                    if sibling.right.color == BLACK:
                        sibling.left.color = BLACK
                        sibling.color = RED
                        self._right_rotate(sibling)
                        sibling = parent.right
                    # CASE ii: right Child is Red
                    sibling.color = parent.color
                    parent.color = sibling.right.color = BLACK
                    self._left_rotate(parent)
                    node = self.root
                else:
                    node.color = BLACK
                    node = parent
            else:
                sibling = parent.left
                if not sibling:
                    break
                # CASE 1: Sibling is RED
                if sibling.color == RED:
                    sibling.color = BLACK
                    parent.color = RED
                    self._right_rotate(parent)
                    sibling = parent.left
                # CASE 2: Sibling is Black
                # CASE A: Both children are also black
                if sibling.left.color == sibling.right.color == BLACK:
                    sibling.color = RED
                    node = parent
                # CASE B: right child is red
                elif sibling.left:
                    # CASE i: left Child Black
                    if sibling.left.color == BLACK:
                        sibling.right.color = BLACK
                        sibling.color = RED
                        self._left_rotate(sibling)
                        sibling = parent.left
                    # CASE ii: left Child is Red
                    sibling.color = parent.color
                    parent.color = sibling.left.color = BLACK
                    self._right_rotate(parent)
                    node = self.root
                else:
                    node.color = BLACK
                    node = parent
        if node:
            node.color = BLACK
