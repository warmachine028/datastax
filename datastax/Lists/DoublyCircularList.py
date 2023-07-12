from typing import Any

from datastax.Lists.DoublyLinkedList import DoublyLinkedList
from datastax.Lists.CircularLinkedList import CircularLinkedList
from datastax.Lists.AbstractLists import DoublyCircularList as AbstractList


class DoublyCircularList(AbstractList, CircularLinkedList, DoublyLinkedList):

    def append(self, data: Any) -> None:
        super().append(data)
        self.head.set_prev(self.tail)
        self.tail.set_next(self.head)

    def insert(self, data: Any) -> None:
        super().insert(data)
        self.head.set_prev(self.tail)
        self.tail.set_next(self.head)
