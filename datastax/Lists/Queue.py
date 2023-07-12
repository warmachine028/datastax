# Queue implementation using LinkedList

from sys import maxsize
from typing import Any, Optional, Sequence, Self
from datastax.Lists.Node import Node
from datastax.errors import OverFlowError, UnderFlowError
from datastax.Lists.LinkedList import LinkedList
from datastax.Lists.AbstractLists import Queue as AbstractQueue


class Queue(AbstractQueue, LinkedList):
    def __init__(self, capacity: Optional[int] = None,
                 items: Optional[list] = None):
        super().__init__()
        self._rear = 0
        self.set_capacity(capacity)
        self._build(items if items else [])

    def _build(self, items: Sequence[Any]) -> Self:
        for item in items[:self.capacity]:
            self.enqueue(item)
        return self

    def is_empty(self) -> bool:
        return self.head is None

    def is_full(self) -> bool:
        return self._rear == self.capacity

    def set_capacity(self, capacity: int | None):
        if capacity is None:
            self._capacity = maxsize
            return
        if not isinstance(capacity, int):
            raise TypeError("The 'capacity' parameter must be an "
                            "instance of int or its subclass.")
        if capacity < 0:
            raise ValueError("Capacity can't be negative")
        self._capacity = capacity

    def enqueue(self, data: Any) -> int:
        if self.is_full():
            raise OverFlowError(self)
        node = Node(data)
        if not self.head:
            self.set_head(node)
        else:
            self.tail.set_next(node)
        self.set_tail(node)
        self._rear += 1
        return 0

    def dequeue(self) -> Any:
        if self.is_empty():
            raise UnderFlowError(self)
        deleted_node = self.head
        deleted_item = deleted_node.data
        self.set_head(self.head.next)
        self._rear -= 1
        return deleted_item

    def peek(self) -> str | Optional[Any]:
        if self.is_empty():
            return "QUEUE EMPTY"
        return self._tail.data if self._tail else None
