from __future__ import annotations

from typing import Any, Optional

from datastax.linkedlists.private_lists.circular_linked_list import (
    CircularLinkedList
)
from datastax.linkedlists.private_lists.doubly_linked_list import (
    DoublyLinkedList
)


class DoublyCircularList(DoublyLinkedList, CircularLinkedList):
    def _construct(self, array: Optional[list[Any]]) -> DoublyCircularList:
        raise NotImplementedError

    def __str__(self):
        if not self.head:
            return 'NULL'
        start_padding = 6
        top = '    '
        mid = ' ╭─'
        dow = ' │  '
        ref = self.head
        max_width = self._max_width(ref) + 4
        nodes = 0
        while ref:
            top += f" ┌────╥{'─' * max_width}╥────┐  "
            mid += f"---->  ║{f'{ref.data}'.center(max_width)}║  <---"
            dow += f" └────╨{'─' * max_width}╨────┘  "
            ref = ref.next
            nodes += 1
            if ref is self.head:
                break

        length_per_node = max_width + 12
        heading = self._draw_heading(nodes, length_per_node, start_padding - 1)
        top += '\n'
        mid = f"{mid}-─╮\n"
        dow += ' │\n'
        footing = self._draw_footing(nodes, length_per_node, start_padding)
        return heading + top + mid + dow + footing
