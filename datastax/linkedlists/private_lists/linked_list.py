from __future__ import annotations

from typing import Any, Optional


# private method to mangle string __repr__
def _mangled(item: Any) -> str:
    if '\n' in str(item):
        return f"{str(type(item))[8:-2].split('.')[-1]}@{id(item)}"
    return str(item)


class Node:
    def __init__(self, data: Any, _next: Node = None):
        self.data = data
        self.next = _next

    def __str__(self):
        width = len(str(self.data)) + 4
        top = f" ┌{'─' * width}╥────┐\n"
        mid = (
            f" │{f'{_mangled(self.data)}'.center(width)}║ ------> "
            f"{'next' if self.next else 'NULL'}\n"
        )
        dow = f" └{'─' * width}╨────┘\n"
        return top + mid + dow

    def __repr__(self):
        return self.__str__()


class LinkedList:
    def __init__(self, array: list[Any] = None, head: Node = None):
        self._head = head
        self._tail = head
        self._construct(array)

    def _construct(self, array: Optional[list[Any]]) -> LinkedList:
        raise NotImplementedError

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @staticmethod
    def _max_width(node: Optional[Node]):
        max_width = 0
        while node:
            max_width = max(max_width, len(_mangled(node.data)))
            node = node.next
        return max_width

    def __str__(self):
        start_padding = 1
        top = mid = dow = ' ' * start_padding
        ref = self.head
        max_width = self._max_width(ref) + 4
        nodes = 0
        while ref:
            top += f"┌{'─' * max_width}╥────┐   "
            mid += f"│{f'{_mangled(ref.data)}'.center(max_width)}║  ----->"
            dow += f"└{'─' * max_width}╨────┘   "
            ref = ref.next
            nodes += 1

        length_per_node = max_width + 7
        heading = self._draw_heading(nodes, length_per_node, start_padding)
        top += '\n'
        mid += f"{' ' if mid[-1] == '>' else ''}NULL\n"
        dow += '\n'

        return heading + top + mid + dow

    def _draw_heading(self, n: int, lpn: int, start_padding: int) -> str:
        if n == 0:
            return ' '
        head, tail = 'HEAD'.center(lpn), 'TAIL'.center(lpn)
        spaces = ' ' * 3
        if self.head is self.tail:
            return (
                f"{' ' * start_padding}{head}\n"
                f"{' ' * start_padding}{tail}\n"
            )
        return (
            f"{' ' * start_padding}"
            f"{head}{' ' * lpn * (n - 2)}"
            f"{spaces * (n - 1)}{tail}\n"
        )

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        ref = self.head
        while ref:
            yield ref.data
            ref = ref.next
