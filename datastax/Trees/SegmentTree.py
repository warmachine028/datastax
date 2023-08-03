from typing import Any, Optional
from datastax.Trees.BinaryTree import BinaryTree
from datastax.Nodes import SegmentNode
from datastax.Trees.AbstractTrees import SegmentTree as AbstractTree


class SegmentTree(BinaryTree, AbstractTree):
    _segment_array = []

    def update_at_range(self, left: int, right: int, data: int) -> None:
        raise NotImplementedError

    def update_at_index(self, index: int, data: int) -> None:
        raise NotImplementedError

    def get_range(self, left: int, right: int,
                  root: SegmentNode | None,
                  lazy_node: SegmentNode | None):
        raise NotImplementedError

    def insert(self, item: Any):
        raise NotImplementedError

    def delete(self, data: Any = None) -> Optional[Any]:
        raise NotImplementedError

    def insert_path(self, data: Any, path: Optional[list[str]] = None) -> None:
        raise NotImplementedError

    def _traverse_leafs(self, node: SegmentNode | None) -> None:
        if not node:
            return None
        if not any((node.left, node.right)):
            return self._segment_array.append(node.data)
        # if left child is found, check for leaf node recursively
        if node.left:
            self._traverse_leafs(node.left)
        # if right child is found, check for leaf node recursively
        if node.right:
            self._traverse_leafs(node.right)
