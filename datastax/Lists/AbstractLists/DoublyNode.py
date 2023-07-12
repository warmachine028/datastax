from abc import ABC
from typing import Optional, Self

from datastax.Lists.AbstractLists.Node import Node
from datastax.Utils import Commons


class DoublyNode(Node, ABC):
    _next: Optional[Self]
    _prev: Optional[Self]

    @property
    def next(self):
        return self._next

    @property
    def prev(self):
        return self._prev

    def __str__(self):
        width = len(Commons.repr(self.data)) + 4
        top = f"        ┌────╥{'─' * width}╥────┐\n"
        mid = (
            f"{' prev' if self.prev else ' NULL'}"
            f" <----  ║{f'{Commons.repr(self.data)}'.center(width)}║  ----> "
            f"{' next' if self.next else ' NULL'}\n"
        )
        dow = f"        └────╨{'─' * width}╨────┘\n"
        return top + mid + dow
