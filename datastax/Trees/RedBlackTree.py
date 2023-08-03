import warnings
from typing import Optional, Any
from datastax.Utils.Warnings import DuplicateNodeWarning
from datastax.Utils import ColorCodes
from datastax.Nodes import RedBlackNode
from datastax.Trees.BinarySearchTree import BinarySearchTree
from datastax.Trees.AbstractTrees import RedBlackTree as AbstractTree

RED, BLACK = ColorCodes.RED, ColorCodes.BLACK


class RedBlackTree(BinarySearchTree, AbstractTree):
    # Private helper function for inserting
    def _place(self,
               parent: Optional[RedBlackNode],
               data) -> Optional[RedBlackNode]:
        node = RedBlackNode(data)
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

        node.set_parent(parent)
        # Node to be added is root node
        if not parent:
            node.set_color(BLACK)
            return node
        if parent.data > node.data:
            parent.set_left(node)
        else:
            parent.set_right(node)
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
        # * Resolve Red-Red Conflict
        parent = node.parent
        if parent and parent.color is RED:
            sibling = self.sibling_of(parent)
            # CASE 1: Recolor and move up to see if more work required.
            if sibling and sibling.color is RED:
                parent.set_color(BLACK)
                sibling.set_color(BLACK)
                if parent.parent and parent.parent is not self.root:
                    parent.parent.set_color(RED)
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
                        parent.set_color(BLACK)
                        parent.parent.set_color(RED)
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
                        parent.set_color(BLACK)
                        parent.parent.set_color(RED)
                        self._left_rotate(parent.parent)

    # Private helper method of balance function to perform RR rotation
    def _right_rotate(self, node: RedBlackNode) -> RedBlackNode:
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
    def _left_rotate(self, node: RedBlackNode) -> RedBlackNode:
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

    # Private helper method for delete to perform exchange of data between node
    def _transplant(self, node: RedBlackNode,
                    new_node: Optional[RedBlackNode]) -> None:
        if not node.parent:
            self.set_root(new_node)
        elif node is node.parent.left:
            node.parent.set_left(new_node)
        else:
            node.parent.set_right(new_node)
        if new_node:
            new_node.set_parent(node.parent)

    def _delete(self, root, item: Any):
        node = self.search(item)
        if not node:
            return node
        color = node.color
        if node.left and node.right:
            predecessor = self.inorder_predecessor(node)
            color = predecessor.color
            pull_up = predecessor.left
            if predecessor.parent is node and pull_up:
                pull_up.set_parent(predecessor)
            else:
                self._transplant(predecessor, pull_up)
                predecessor.set_left(node.left)
                if node.left:
                    node.left.set_parent(predecessor)
            self._transplant(node, predecessor)
            predecessor.set_right(node.right)
            if node.right:
                node.right.set_parent(predecessor)
            predecessor.set_color(node.color)
        else:
            pull_up = node.left if node.left else node.right
            self._transplant(node, pull_up)

        if color is BLACK:
            self._post_delete(pull_up)

        return self.root

    def _resolve_left_black_conflict(self, node: RedBlackNode) -> RedBlackNode:
        parent = node.parent
        sibling = parent.right
        if sibling.color is RED:
            sibling.set_color(BLACK)
            parent.set_color(RED)
            self._left_rotate(parent)
            sibling = node.parent.right

        if sibling.left.color is BLACK and sibling.right.color is BLACK:
            sibling.set_color(RED)
            node = parent
        else:
            if sibling.right.color is BLACK:
                sibling.left.set_color(BLACK)
                sibling.set_color(RED)
                self._right_rotate(sibling)
                sibling = parent.right

            sibling.set_color(parent.color)
            parent.set_color(BLACK)
            sibling.right.set_color(BLACK)
            self._left_rotate(parent)
            node = self.root

        return node

    def _resolve_right_black_conflict(self,
                                      node: RedBlackNode) -> RedBlackNode:
        parent = node.parent
        sibling = parent.left
        if sibling.color is RED:
            sibling.set_color(BLACK)
            parent.set_color(RED)
            self._right_rotate(parent)
            sibling = parent.left

        if sibling.right.color is sibling.left.color is BLACK:
            sibling.set_color(RED)
            node = parent
        else:
            if sibling.left.color is BLACK:
                sibling.right.set_color(BLACK)
                sibling.set_color(RED)
                self._left_rotate(sibling)
                sibling = parent.left

            sibling.set_color(parent.color)
            parent.set_color(BLACK)
            sibling.left.set_color(BLACK)
            self._right_rotate(parent)
            node = self.root
        return node

    def _post_delete(self, node: Optional[RedBlackNode]):
        # ! Resolve Double Black sentinel Conflict
        while node and node is not self.root and node.color is BLACK:
            parent = node.parent
            if not parent:
                break
            if node is parent.left:
                node = self._resolve_left_black_conflict(node)
            else:
                node = self._resolve_right_black_conflict(node)
        if node:
            node.set_color(BLACK)
