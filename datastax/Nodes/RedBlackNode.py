from typing import Self, Optional, Any
from datastax.Nodes.TreeNode import TreeNode
from datastax.Nodes.AbstractNodes import RedBlackNode as AbstractNode
from datastax.Utils import ColorCodes


class RedBlackNode(TreeNode, AbstractNode):
    def __init__(self, data: Any,
                 left: Optional[Self] = None,
                 right: Optional[Self] = None,
                 color: int = ColorCodes.RED):
        super().__init__(data, left, right)
        self.set_color(color)

    def set_parent(self, parent: Self | None):
        if parent is None or isinstance(parent, RedBlackNode):
            self._parent = parent
            return
        raise TypeError("The 'parent' parameter must be an "
                        "instance of RedBlackNode or its subclass.")

    def set_color(self, color: int):
        if color in (0, 1):
            self._color = color
            return
        raise TypeError("The 'color' parameter must be 0 or 1")
