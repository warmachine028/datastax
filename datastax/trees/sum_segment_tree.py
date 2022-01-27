# Sum Segment Tree implementation
from __future__ import annotations

from typing import Any, Optional

from datastax.trees.private_trees.segment_tree import SegmentTree, SegmentNode


class SumSegmentTree(SegmentTree):
    def insert(self, item: Any):
        raise NotImplementedError

    def _construct(self, array: list[Any] = None) -> Optional[SumSegmentTree]:
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
            node.data = node.left.data + node.right.data
            return node

        self._root = build(0, len(array) - 1)
        return self

    def get_sum(self, left: int, right: int, root: SegmentNode = None):
        if not root:
            root = self.root
        if not root:
            return None
        if root.left_index >= left and root.right_index <= right:
            return root.data
        if root.right_index < left or root.left_index > right:
            if isinstance(root.data, int):
                return 0
            if isinstance(root.data, str):
                return ""
            return []
        return (
                self.get_sum(left, right, root.left)
                +
                self.get_sum(left, right, root.right)
        )

    def update_at_index(self, index: int, data: Any,
                        root: SegmentNode = None):
        def update(node, idx, new):
            if idx == node.left_index == node.right_index:
                difference = node.left_index
                if isinstance(node.data, int):
                    difference = new - node.data
                node.data = new
                return difference
            mid = (node.left_index + node.right_index) // 2
            if idx <= mid:
                difference = update(node.left, idx, new)
            else:
                difference = update(node.right, idx, new)
            if isinstance(node.data, int):
                node.data += difference
            if isinstance(node.data, str) or isinstance(node.data, list):
                _index = difference  # node.data.index(*difference)
                node.data = node.data[:_index] + new + node.data[_index + 1:]
            return difference

        if not root:
            root = self.root
        if not root:
            return
        update(root, index, data)


if __name__ == '__main__':
    arr = [*range(10)]
    print(SumSegmentTree(arr))
