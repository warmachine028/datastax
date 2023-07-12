from typing import Any, Optional, Self, Iterable
from datastax.Lists.AbstractLists.Node import Node
from datastax.Utils import Commons
from abc import abstractmethod, ABC as AbstractClass


class LinkedList(AbstractClass):
    _head: Optional[Node] = None
    _tail: Optional[Node] = None

    def _max_width(self, node: Optional[Node]):
        max_width = 0
        while node:
            max_width = max(max_width, len(Commons.repr(node.data)))
            node = node.next
        return max_width

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def __str__(self):
        start_padding = 1
        top = mid = dow = " " * start_padding
        ref = self.head
        max_width = self._max_width(ref) + 4
        nodes = 0
        while ref:
            top += f"┌{'─' * max_width}╥────┐   "
            mid += f"│{f'{Commons.repr(ref.data)}'.center(max_width)}║  ----->"
            dow += f"└{'─' * max_width}╨────┘   "
            ref = ref.next
            nodes += 1

        length_per_node = max_width + 7
        heading = self._draw_heading(nodes, length_per_node, start_padding)
        top += "\n"
        mid += f"{' ' if mid[-1] == '>' else ''}NULL\n"
        dow += "\n"

        return heading + top + mid + dow

    def _draw_heading(self, n: int, lpn: int, start_padding: int) -> str:
        if n == 0:
            return " "
        head, tail = "HEAD".center(lpn), "TAIL".center(lpn)
        spaces = " " * 3
        if self._head is self._tail:
            return f"{' ' * start_padding}{head}\n" \
                   f"{' ' * start_padding}{tail}\n"
        return (
            f"{' ' * start_padding}"
            f"{head}{' ' * lpn * (n - 2)}"
            f"{spaces * (n - 1)}{tail}\n"
        )

    @abstractmethod
    def append(self, data: Any) -> None:
        ...

    @abstractmethod
    def insert(self, data: Any) -> None:
        ...

    @abstractmethod
    def _construct(self, array: Iterable[Any]) -> Self:
        ...
