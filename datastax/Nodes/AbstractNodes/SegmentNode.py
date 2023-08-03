from datastax.Nodes.AbstractNodes.TreeNode import TreeNode
from abc import ABC as AbstractClass


class SegmentNode(TreeNode, AbstractClass):
    left_index: int
    right_index: int

    def __str__(self):
        # to be overriden and implemented later
        return super().__str__()

    def preorder_print(self) -> None:
        # to be overriden and implemented later
        super().preorder_print()
