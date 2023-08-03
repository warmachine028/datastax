from typing import Any, Self, Optional
from datastax.Nodes.TreeNode import TreeNode
from datastax.Nodes.AbstractNodes import SegmentNode as AbstractNode


class SegmentNode(TreeNode, AbstractNode):
    left_index = 0
    right_index = 0

    def __init__(self, data: Any,
                 left: Optional[Self] = None,
                 right: Optional[Self] = None):
        super().__init__(data, left, right)
