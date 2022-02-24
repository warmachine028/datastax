from __future__ import annotations

from typing import Any, Optional

from datastax.linkedlists.private_lists import doubly_linked_list
from datastax.linkedlists.private_lists.doubly_linked_list import DoublyNode


class DoublyLinkedList(doubly_linked_list.DoublyLinkedList):
    def _construct(self, array: Optional[list[Any]]) -> DoublyLinkedList:
        if array and array[0] is not None:
            for item in array:
                self.append(item)
        return self

    def append(self, data) -> None:
        node = DoublyNode(data, None, self.tail)
        if not self.head:
            self._head = node
        else:
            self.tail.next = node
        self._tail = node

    def insert(self, data: Any):
        node = DoublyNode(data, self.head)
        if self.head:
            self.head.prev = node
        if not self.tail:
            self._tail = node
        self._head = node
