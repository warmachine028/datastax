# Sum Segment Tree implementation
from __future__ import annotations

from sys import maxsize
from typing import Any, Optional

from datastax.trees.private_trees.segment_tree import SegmentTree, SegmentNode


class MinSegmentTree(SegmentTree):
    def insert(self, item: Any):
        raise NotImplementedError

    def _construct(self, array: list[Any] = None) -> Optional[MinSegmentTree]:
        if not array or array[0] is None:
            return None

        def build(left: int, right: int) -> SegmentNode:
            node = SegmentNode(None)
            # Leaf Node
            if array and left == right:
                node.left_index, node.right_index = left, right
                node.data = array[left]
                return node
            # Intermediate Node
            mid = (left + right) // 2
            node.left, node.right = build(left, mid), build(mid + 1, right)
            node.left_index = node.left.left_index
            node.right_index = node.right.right_index
            node.data = min(node.left.data, node.right.data)
            return node

        self._root = build(0, len(array) - 1)
        return self

    def get_min(self, left: int, right: int, root: SegmentNode = None):
        if not root:
            root = self.root
        if not root:
            return None
        if root.left_index >= left and root.right_index <= right:
            return root.data
        if right < root.left_index or root.right_index < left:
            if isinstance(root.data, int):
                return maxsize
            if isinstance(root.data, str):
                return "z"  # chr(1114099)
            return [maxsize]
        return min(
            self.get_min(left, right, root.left),
            self.get_min(left, right, root.right)
        )

    def update_at_index(self, index: int, data: Any,
                        root: SegmentNode = None):
        def update(node, idx, new):
            if not node:
                return
            if idx == node.left_index == node.right_index:
                node.data = new
            mid = (node.left_index + node.right_index) // 2
            update(node.left if idx <= mid else node.right, idx, new)
            node.data = min(node.left.data if node.left else node.data,
                            node.right.data if node.right else node.data)

        if not root:
            root = self.root
        if not root:
            return
        update(root, index, data)
