from typing import Any, Self, Optional
from datastax.Nodes.TreeNode import TreeNode


class SplayNode(TreeNode):
    _parent: Optional[Self] = None

    def __init__(self, data: Any,
                 left: Optional[Self] = None,
                 right: Optional[Self] = None):
        super().__init__(data, left, right)

    @property
    def parent(self):
        return self._parent

    def set_parent(self, parent: Self | None):
        if parent is None or isinstance(parent, SplayNode):
            self._parent = parent
            return
        raise TypeError("The 'parent' parameter must be an "
                        "instance of SplayNode or its subclass.")
