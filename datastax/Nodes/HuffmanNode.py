from typing import Self, Any, Optional
from datastax.Nodes.TreeNode import TreeNode
from datastax.Nodes.AbstractNodes import HuffmanNode as AbstractNode


class HuffmanNode(TreeNode, AbstractNode):
    def __init__(self, data: Any,
                 left: Optional[Self] = None,
                 right: Optional[Self] = None,
                 frequency: Optional[int] = 1):
        super().__init__(data, left, right)
        self.set_frequency(1 if frequency is None else frequency)

    def set_frequency(self, frequency: int):
        if isinstance(frequency, int):
            self._frequency = frequency
            return
        raise TypeError("The 'frequency' parameter must be an "
                        "instance of HuffmanNode or its subclass.")
