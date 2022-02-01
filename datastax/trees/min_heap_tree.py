# Min Heap Tree Implementation
from __future__ import annotations

from datastax.trees.heap_tree import HeapTree, HeapNode


class MinHeapTree(HeapTree):
    def _heapify(self, node: HeapNode) -> None:
        if node.parent and node.parent.data > node.data:
            node.parent.data, node.data = node.data, node.parent.data
            self._heapify(node.parent)

    def _shift_up(self, node: HeapNode) -> None:
        root = node
        left_child = root.left
        right_child = root.right
        if left_child and left_child.data < root.data:
            root = left_child
        if right_child and right_child.data < root.data:
            root = right_child
        if root is node:
            return
        root.data, node.data = node.data, root.data
        self._shift_up(root)
