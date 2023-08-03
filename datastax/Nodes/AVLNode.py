from typing import Any, Self, Optional
from datastax.Nodes.TreeNode import TreeNode


class AVLNode(TreeNode):
    _height = 1

    def __init__(self, data: Any,
                 left: Optional[Self] = None,
                 right: Optional[Self] = None):
        super().__init__(data, left, right)

    @property
    def height(self):
        return self._height

    def set_height(self, height: int):
        if isinstance(height, int):
            self._height = height
            return
        raise TypeError("The 'height' parameter must be an integer")
