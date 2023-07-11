# Queue implementation using LinkedList

from sys import maxsize
from typing import Any
from datastax.Lists import Node
from datastax.errors import OverFlowError, UnderFlowError
from datastax.Lists import LinkedList
from datastax.Lists.AbstractLists import Queue as AbstractQueue


class Queue(AbstractQueue, LinkedList):
    def __init__(self, capacity: int = None, items: list[Any] = None):
        super().__init__()
        self._rear = 0
        self.set_capacity(capacity)
        if items:
            for item in items[:self.capacity]:
                self.enqueue(item)

    def is_empty(self) -> bool:
        return self.head is None

    def is_full(self) -> bool:
        return self._rear == self.capacity

    def set_capacity(self, capacity: int):
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

    def peek(self) -> str:
        if self.is_empty():
            return "QUEUE EMPTY"
        return str(self._tail.data if self._tail else None)

    def append(self, data: Any) -> None:
        raise NotImplementedError

    def insert(self, data: Any) -> None:
        raise NotImplementedError
