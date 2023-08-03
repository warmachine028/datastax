import warnings
from typing import Any, Optional, Self, Sequence

from datastax.Utils.Warnings import DeletionFromEmptyTreeWarning
from datastax.Trees.BinaryTree import BinaryTree
from datastax.Nodes import HeapNode


class HeapTree(BinaryTree):
    _leaf: Optional[HeapNode]

    def __init__(self, items: Optional[list] = None,
                 root: Optional[HeapNode] = None):
        self.set_root(root)
        self.set_leaf(root)
        super().__init__(items, root)

    @property
    def leaf(self):
        return self._leaf

    def set_leaf(self, leaf: HeapNode | None):
        if leaf is None or isinstance(leaf, HeapNode):
            self._leaf = leaf
            return
        raise TypeError("The 'leaf' parameter must be an "
                        "instance of HeapNode or its subclass.")

    def _construct(self, items: Optional[Sequence] = None) -> Self | None:
        if not items or items[0] is None:
            return None

        for item in items:
            try:
                self.heappush(item)
            except TypeError as error:
                raise error
        return self

    # Function to push an element inside a tree
    def heappush(self, data: Any) -> None:
        root = self.root
        if data is None:
            return
        node = HeapNode(data)
        if root is None:  # Heap Tree is Empty
            self.set_root(node)
            self.set_leaf(node)
        # Heap tree has nodes. So inserting new node
        # in the left of leftmost leaf node
        elif self.leaf and self.leaf.left is None:
            self.leaf.set_left(node)
            node.set_parent(self.leaf)
        else:
            if not self.leaf:
                return
            self.leaf.set_right(node)
            previous_leaf = self.leaf
            node.set_parent(previous_leaf)
            self._update_leaf(self.leaf)
            self.leaf.set_prev_leaf(previous_leaf)
        self._heapify(node)

    # Private function to convert a subtree to heap
    def _heapify(self, node: HeapNode) -> None:
        if node.parent and node.parent.data < node.data:
            node.parent.data, node.data = node.data, node.parent.data
            self._heapify(node.parent)

    # Private Helper method of heappush function to
    # update rightmost node in the deepest level
    def _update_leaf(self, node: HeapNode) -> None:
        # reach extreme left of next level if current level is full
        if node.parent is None:
            self.set_leaf(node)
        elif node.parent.left is node:
            self.set_leaf(node.parent.right)
        elif node.parent.right is node:
            self._update_leaf(node.parent)
        while self.leaf and self.leaf.left:
            self.set_leaf(self.leaf.left)

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
            self.set_root(None)
            self.set_leaf(None)
        else:
            if self.leaf.right and self.root:
                self.root.data = self.leaf.right.data
                self.leaf.set_right(None)
                self._shift_up(self.root)
            elif self.leaf.left and self.root:
                self.root.data = self.leaf.left.data
                self.leaf.set_left(None)
                self._shift_up(self.root)
            else:  # We have reached the end of a level
                self.set_leaf(self.leaf.prev_leaf)
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
