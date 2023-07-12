from typing import Any

from datastax.Lists.LinkedList import LinkedList
from datastax.Lists.AbstractLists import CircularLinkedList as AbstractList


class CircularLinkedList(AbstractList, LinkedList):
    def append(self, data: Any) -> None:
        super().append(data)
        self.tail.set_next(self.head)

    def insert(self, data: Any):
        super().insert(data)
        self.tail.set_next(self.head)

    def __iter__(self):
        ref = self.head
        while ref:
            yield ref.data
            ref = ref.next
            if ref is self.head:
                break
