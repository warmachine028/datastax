from typing import Any, Self, Optional

from datastax.Lists.AbstractLists import Node as AbstractNode


class Node(AbstractNode):
    def __init__(self, data: Any,
                 _next: Optional[Self] = None):
        self.data = data
        self.set_next(_next)

    def set_next(self, _next: Optional[Self] = None):
        if _next is None or isinstance(_next, Node):
            self._next = _next
            return
        raise TypeError("The 'next' parameter must be an "
                        "instance of Node or its subclass.")
