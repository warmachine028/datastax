from __future__ import annotations

from typing import Any, Optional

from datastax.linkedlists.private_lists.linked_list import Node, LinkedList


class DoublyNode(Node):
    def __init__(self, data: Any, _next: DoublyNode = None,
                 prev: DoublyNode = None):
        super().__init__(data, _next)
        self.next: Optional[DoublyNode] = _next
        self.prev: Optional[DoublyNode] = prev

    def __str__(self):
        width = len(str(self.data)) + 4
        top = f"        ┌────╥{'─' * width}╥────┐\n"
        mid = (
            f"{' prev' if self.next else ' NULL'}"
            f" <----  ║{f'{self.data}'.center(width)}║  ----> "
            f"{' next' if self.next else ' NULL'}\n"
        )
        dow = f"        └────╨{'─' * width}╨────┘  "
        return top + mid + dow

    def __repr__(self):
        return self.__str__()


class DoublyLinkedList(LinkedList):
    def __init__(self, array: list[Any] = None, head: DoublyNode = None):
        super().__init__(array, head)
        self._head: DoublyNode = self.head
        self._tail: DoublyNode = self.tail

    def _construct(self, array: Optional[list[Any]]) -> DoublyLinkedList:
        raise NotImplementedError

    def __str__(self):
        string = " NULL <"
        start_padding = 8
        bottom = top = " " * start_padding
        nodes = 0
        ref = self.head
        max_width = self._max_width(ref) + 4
        while ref:
            top += f" ┌────╥{'─' * max_width}╥────┐  "
            next_ptr = '<' if ref.next else '-'
            prev_ptr = '>' if ref.prev else '-'
            string += f"----{prev_ptr}" \
                      f"  ║{str(ref.data).center(max_width)}║  " \
                      f"{next_ptr}---"
            bottom += f" └────╨{'─' * max_width}╨────┘  "
            ref = ref.next
            nodes += 1

        length_per_node = max_width + 12
        heading = self._draw_heading(nodes, length_per_node, start_padding)
        top += '\n'
        string = f"{string}-> NULL\n" if nodes else f"{string[:-1]}\n"
        bottom += '\n'
        return heading + top + string + bottom
