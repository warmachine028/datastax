from typing import Any, Optional, Self
from datastax.Nodes.AbstractNodes import TreeNode as AbstractNode


class TreeNode(AbstractNode):
    def __init__(self, data: Any,
                 left: Optional[Self] = None,
                 right: Optional[Self] = None):
        self.data = data
        self.set_left(left)
        self.set_right(right)

    def set_left(self, left: Self | None):
        if left is None or isinstance(left, TreeNode):
            self._left = left
            return
        raise TypeError("The 'left' parameter must be an "
                        "instance of TreeNode or its subclass.")

    def set_right(self, right: Self | None):
        if right is None or isinstance(right, TreeNode):
            self._right = right
            return
        raise TypeError("The 'right' parameter must be an "
                        "instance of TreeNode or its subclass.")
