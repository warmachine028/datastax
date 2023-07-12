from typing import Self, Optional, Any
from datastax.Utils import Commons
from abc import ABC as AbstractClass, abstractmethod


class Node(AbstractClass):
    data: Optional[Any]
    _next: Optional[Self]

    @property
    def next(self):
        return self._next

    def __str__(self):
        width = len(Commons.repr(self.data)) + 4
        top = f" ┌{'─' * width}╥────┐\n"
        mid = (
            f" │{f'{Commons.repr(self.data)}'.center(width)}║ ------> "
            f"{'next' if self.next else 'NULL'}\n"
        )
        dow = f" └{'─' * width}╨────┘\n"
        return top + mid + dow

    @abstractmethod
    def set_next(self, _next: Optional[Self]):
        ...
