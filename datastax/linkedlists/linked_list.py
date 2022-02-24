from __future__ import annotations

from typing import Any, Optional

from datastax.linkedlists.private_lists import linked_list
from datastax.linkedlists.private_lists.linked_list import Node


class LinkedList(linked_list.LinkedList):
    def _construct(self, array: Optional[list[Any]]) -> LinkedList:
        if array and array[0] is not None:
            for item in array:
                self.append(item)
        return self

    def append(self, data: Any) -> None:
        node = Node(data)
        if not self.head:
            self._head = node
        else:
            self.tail.next = node
        self._tail = node

    def insert(self, data: Any):
        node = Node(data, self.head)
        if not self.tail:
            self._tail = node
        self._head = node
