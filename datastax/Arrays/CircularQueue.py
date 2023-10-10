# Circular Queue implementation using Lists (Pseudo Arrays)
from typing import Any, Optional

from datastax.Utils.Exceptions import OverflowException, UnderflowException
from datastax.Arrays import Queue


class CircularQueue(Queue):
    def __init__(self, *, capacity: Optional[int] = None):
        super().__init__(capacity=capacity)
        self._front = 0
        self._rear = 0 

    def is_full(self) -> bool:
        if not super().is_full():
            return False
        return (self._rear + 1) % self.capacity == self._front

    def is_empty(self) -> bool:
        if super().is_empty():
            return True
        return self._front == self._rear

    def enqueue(self, item: Any) -> int:
        if self.is_full():
            raise OverflowException(self)
        
        if not super().is_full():
            self._array.append(item) 
        else:
            self._array[self._rear] = item
        self._rear = (self._rear + 1) % self.capacity
        return 0

    def dequeue(self) -> Any:
        if self.is_empty():
            raise UnderflowException(self)
        deleted_item = self._array[self.front]
        self._front = (self._front + 1) % self.capacity
        return deleted_item

    def peek(self) -> Any:
        if self.is_empty():
            return "CIRCULAR QUEUE EMPTY"
        return self._array[self._front]
