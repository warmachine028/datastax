from typing import Any, Optional, Self

from datastax.Lists import DoublyLinkedList
from datastax.Lists.AbstractLists import DoublyCircularList as AbstractList


class DoublyCircularList(AbstractList, DoublyLinkedList):

    def _construct(self, array: Optional[list[Any]]) -> Self:
        if array and array[0] is not None:
            for item in array:
                self.append(item)
        return self

    def append(self, data: Any) -> None:
        super().append(data)
        self.head.set_prev(self.tail)
        self.tail.set_next(self.head)

    def insert(self, data: Any) -> None:
        super().insert(data)
        self.head.set_prev(self.tail)
        self.tail.set_next(self.head)
