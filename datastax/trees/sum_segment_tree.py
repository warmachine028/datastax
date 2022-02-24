# Sum Segment Tree implementation
from __future__ import annotations

from typing import Any, Optional

from datastax.trees.private_trees.segment_tree import SegmentTree, SegmentNode


class SumSegmentTree(SegmentTree):
    def __init__(self, array=None, root=None):
        self._lazy_tree = SegmentTree()
        super().__init__(array, root)

    def insert(self, item: Any):
        raise NotImplementedError

    @property
    def lazy_tree(self):
        return self._lazy_tree

    def _construct(self, array: list[int] = None) -> Optional[SumSegmentTree]:
        if not array or array[0] is None:
            return None

        def build(left: int, right: int) -> tuple[SegmentNode, ...]:
            node, lazy_node = SegmentNode(None), SegmentNode(0)
            # Leaf Node
            if array and left == right:
                node.left_index, node.right_index = left, right
                lazy_node.left_index, lazy_node.right_index = left, right
                node.data = array[left]
                return node, lazy_node
            # Intermediate Node
            mid = (left + right) // 2
            node.left, lazy_node.left = build(left, mid)
            node.right, lazy_node.right = build(mid + 1, right)
            node.left_index = lazy_node.left_index = node.left.left_index
            node.right_index = lazy_node.right_index = node.right.right_index
            node.data = sum((node.left.data, node.right.data))
            return node, lazy_node

        self._root, self._lazy_tree._root = build(0, len(array) - 1)
        return self

    @staticmethod
    def _perform_lazy_update(root: SegmentNode, lazy_node: SegmentNode,
                             start: int, end: int, nodes: int) -> None:
        # has lazy values, needs to be propagated
        if lazy_node.data:
            root.data += lazy_node.data * nodes
            if start != end:
                lazy_node.left.data += lazy_node.data
                lazy_node.right.data += lazy_node.data
            # No longer a lazy node
            lazy_node.data = 0

    def get_sum(self, left: int, right: int,
                root: SegmentNode = None,
                lazy_node: SegmentNode = None) -> int:
        if not root:
            root = self.root
            lazy_node = self.lazy_tree.root
        if not root or not lazy_node:
            return 0

        start, end = root.left_index, root.right_index
        nodes = end - start + 1

        # perform lazy update
        self._perform_lazy_update(root, lazy_node, start, end, nodes)

        # location out of bounds
        if end < left or start > right or end < start:
            return 0

        if root.left_index >= left and root.right_index <= right:
            return root.data

        return sum((
            self.get_sum(left, right, root.left, lazy_node.left),
            self.get_sum(left, right, root.right, lazy_node.right)
        ))

    def update_at_range(self, left: int, right: int, data: int) -> None:
        if not self.root:
            return None

        def update(node: SegmentNode, lazy_node: SegmentNode) -> None:
            # How many leaf node values to propagate
            start, end = node.left_index, node.right_index
            nodes = end - start + 1
            # lazy propagation
            self._perform_lazy_update(node, lazy_node, start, end, nodes)

            # location out of bounds
            if end < left or start > right or end < start:
                return

            # location is perfectly in bounds
            if left <= start <= end <= right:
                node.data += data * nodes
                # Mark its children lazy, no need to propagate further
                if start != end:
                    lazy_node.left.data += data
                    lazy_node.right.data += data
                return

            # location is partially in bounds
            update(node.left, lazy_node.left)
            update(node.right, lazy_node.right)
            node.data = sum((node.left.data, node.right.data))

        update(self.root, self.lazy_tree.root)

    def update_at_index(self, index: int, data: int) -> None:
        if not self.root:
            return None

        def update(node: SegmentNode, new: int):
            if index == node.left_index == node.right_index:
                difference = new - node.data
                node.data = new
                return difference
            mid = (node.left_index + node.right_index) // 2
            update_node = node.left if index <= mid else node.right
            difference = update(update_node, new)
            node.data += difference
            return difference

        update(self.root, data)


if __name__ == '__main__':
    tree = SumSegmentTree([2, 3, 1, 4, 2, 5, 2, 3, 1, 5])
    # tree = SumSegmentTree()
    print(tree)
    tree.update_at_range(3, 9, +5)
    print(tree)
    tree.update_at_range(5, 8, +3)
    print(tree.get_sum(3, 5))
    print(tree)
    print(tree.lazy_tree)
    print(tree.segment_array)
    # print(tree)
    # print(tree.lazy_tree)
