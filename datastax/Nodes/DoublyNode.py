from typing import Any, Self, Optional
from datastax.Nodes.Node import Node
from datastax.Nodes.AbstractNodes import DoublyNode as AbstractNode


class DoublyNode(Node, AbstractNode):
    def __init__(self, data: Any,
                 _next: Optional[Self] = None,
                 prev: Optional[Self] = None):
        super().__init__(data)
        self.set_next(_next)
        self.set_prev(prev)

    def set_next(self, _next: Optional[Self]):
        if _next is None or isinstance(_next, DoublyNode):
            super().set_next(_next)
            return
        raise TypeError("The 'next' parameter must be an "
                        "instance of DoublyNode or its subclass.")

    def set_prev(self, prev: Optional[Self]):
        if prev is None or isinstance(prev, DoublyNode):
            self._prev = prev
            return
        raise TypeError("The 'prev' parameter must be an "
                        "instance of DoublyNode or its subclass.")
