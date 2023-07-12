from abc import ABC
from typing import Optional
from datastax.Lists.AbstractLists.LinkedList import LinkedList
from datastax.Utils import Commons
from datastax.Lists.AbstractLists.DoublyNode import DoublyNode


class DoublyLinkedList(LinkedList, ABC):
    _head: Optional[DoublyNode] = None
    _tail: Optional[DoublyNode] = None

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
            string += (
                f"----{prev_ptr}"
                f"  ║{Commons.repr(ref.data).center(max_width)}║  "
                f"{next_ptr}---"
            )
            bottom += f" └────╨{'─' * max_width}╨────┘  "
            ref = ref.next
            nodes += 1

        length_per_node = max_width + 12
        heading = self._draw_heading(nodes, length_per_node, start_padding)
        top += '\n'
        string = f"{string}-> NULL\n" if nodes else f"{string[:-1]}\n"
        bottom += '\n'
        return heading + top + string + bottom
