from typing import Any, Self, Optional

from datastax.Lists.Node import Node
from datastax.Lists.AbstractLists import DoublyNode as AbstractNode


class DoublyNode(AbstractNode, Node):
    def __init__(self, data: Any,
                 _next: Optional[Self] = None,
                 prev: Optional[Self] = None):
        super().__init__(data)
        self.set_next(_next)
        self.set_prev(prev)

    def set_next(self, _next: Optional[Self] = None):
        if _next is not None and not isinstance(_next, DoublyNode):
            raise TypeError("The 'next' parameter must be an "
                            "instance of DoublyNode or its subclass.")
        super().set_next(_next)

    def set_prev(self, prev: Optional[Self] = None):
        if prev is None or isinstance(prev, DoublyNode):
            self._prev = prev
            return
        raise TypeError("The 'prev' parameter must be an "
                        "instance of DoublyNode or its subclass.")
