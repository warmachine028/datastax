from typing import Any, Self, Optional
from datastax.Nodes.TreeNode import TreeNode


class HeapNode(TreeNode):
    _parent: Optional[Self] = None
    _prev_leaf: Optional[Self] = None

    def __init__(self, data: Any,
                 left: Optional[Self] = None,
                 right: Optional[Self] = None):
        super().__init__(data, left, right)

    @property
    def parent(self):
        return self._parent

    @property
    def prev_leaf(self):
        return self._prev_leaf

    def set_parent(self, parent: Self | None):
        if parent is None or isinstance(parent, HeapNode):
            self._parent = parent
            return
        raise TypeError("The 'parent' parameter must be an "
                        "instance of HeapNode or its subclass.")

    def set_prev_leaf(self, prev_leaf: Self | None):
        if prev_leaf is None or isinstance(prev_leaf, HeapNode):
            self._prev_leaf = prev_leaf
            return
        raise TypeError("The 'prev_leaf' parameter must be an "
                        "instance of HeapNode or its subclass.")
