from __future__ import annotations

from typing import Any, Optional

from datastax.linkedlists.private_lists.linked_list import (
    Node,
    LinkedList,
    _mangled
)


class CircularLinkedList(LinkedList):
    def _construct(self, array: Optional[list[Any]]) -> CircularLinkedList:
        raise NotImplementedError

    @staticmethod
    def _max_width(node: Optional[Node]):
        max_width = 0
        ref = node
        while ref:
            max_width = max(max_width, len(_mangled(ref.data)))
            ref = ref.next
            if ref is node:
                break
        return max_width

    def __str__(self):
        if not self.head:
            return 'NULL'
        start_padding = 6
        top = ' ' * start_padding
        mid = ' ╭─-->'
        dow = ' │    '
        ref = self.head
        max_width = self._max_width(ref) + 4
        nodes = 0
        while ref:
            top += f"┌{'─' * max_width}╥────┐   "
            mid += (
                f"│{f'{_mangled(ref.data)}'.center(max_width)}║  "
                f"{('-' if ref.next != self.head else '─') * 5}>"
            )
            dow += f"└{'─' * max_width}╨────┘   "
            ref = ref.next
            nodes += 1
            if ref is self.head:
                break

        length_per_node = max_width + 7
        heading = self._draw_heading(nodes, length_per_node, start_padding)
        top += '\n'
        mid = f"{mid[:-1]}╮\n"
        dow = f'{dow[:-1]}│\n'
        footing = self._draw_footing(nodes, length_per_node, start_padding)
        return heading + top + mid + dow + footing

    @staticmethod
    def _draw_footing(n: int, lpn: int, start_padding: int) -> str:
        if n == 0:
            return ' '
        spaces = '─' * 3
        return (
            f" ╰{'─' * (start_padding - 2)}{'─' * lpn * n}"
            f"{spaces * (n - 1)}──╯\n"
        )

    def __iter__(self):
        ref = self.head
        while ref:
            yield ref.data
            ref = ref.next
            if ref is self.head:
                break
