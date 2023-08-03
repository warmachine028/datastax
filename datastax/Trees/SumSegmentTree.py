from typing import Optional, Self, Sequence
from datastax.Trees.SegmentTree import SegmentTree
from datastax.Nodes import SegmentNode


class SumSegmentTree(SegmentTree):
    _lazy_tree = SegmentTree()

    def __init__(self, items: Optional[Sequence] = None,
                 root: Optional[SegmentNode] = None):
        super().__init__(items, root)

    @property
    def lazy_tree(self):
        return self._lazy_tree

    def _construct(self, array: Optional[Sequence] = None) -> Self | None:
        if not array or array[0] is None:
            return None

        def build(left: int, right: int) -> tuple[SegmentNode, SegmentNode]:
            node, lazy_node = SegmentNode(None), SegmentNode(0)
            # Leaf Node
            if array and left == right:
                node.left_index, node.right_index = left, right
                lazy_node.left_index, lazy_node.right_index = left, right
                node.data = array[left]
                return node, lazy_node
            # Intermediate Node
            mid = (left + right) // 2
            left_node, lazy_left_node = build(left, mid)
            right_node, lazy_right_node = build(mid + 1, right)
            node.set_left(left_node), lazy_node.set_left(lazy_left_node)
            node.set_right(right_node), lazy_node.set_right(lazy_right_node)
            node.left_index = lazy_node.left_index = node.left.left_index
            node.right_index = lazy_node.right_index = node.right.right_index
            node.data = sum((node.left.data, node.right.data))
            return node, lazy_node

        root, lazy_root = build(0, len(array) - 1)
        self.set_root(root), self.lazy_tree.set_root(lazy_root)
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

    def get_sum(self, left: int, right: int) -> int:
        return self.get_range(left, right, self.root, self.lazy_tree.root)

    def get_range(self, left: int, right: int,
                  root: SegmentNode | None,
                  lazy_node: SegmentNode | None) -> int:
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
            self.get_range(left, right, root.left, lazy_node.left),
            self.get_range(left, right, root.right, lazy_node.right)
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
                    lazy_node.left.data += node.data
                    lazy_node.right.data += node.data
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
