from typing import Self, Optional, Any
from datastax.Nodes.TreeNode import TreeNode
from datastax.Nodes.AbstractNodes import ThreadedNode as AbstractNode


class ThreadedNode(TreeNode, AbstractNode):
    def __init__(self, data: Any,
                 left: Optional[Self] = None,
                 right: Optional[Self] = None):
        super().__init__(data, left, right)
        self.set_left_is_child(bool(self.left))
        self.set_right_is_child(bool(self.right))

    def set_left_is_child(self, is_child: bool):
        if isinstance(is_child, bool):
            self._left_is_child = is_child
            return
        raise TypeError("The 'is_child' parameter must be bool")

    def set_right_is_child(self, is_child: bool):
        if isinstance(is_child, bool):
            self._right_is_child = is_child
            return
        raise TypeError("The 'is_child' parameter must be bool")
