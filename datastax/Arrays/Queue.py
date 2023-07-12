# Queue Implementation using Lists (Pseudo Arrays)
from typing import Any

from datastax.errors import OverFlowError, UnderFlowError
from datastax.Arrays.AbstractArrays import Queue as AbstractQueue


class Queue(AbstractQueue):
    def __init__(self, *, capacity: int = None):
        self.set_capacity(capacity)

    def is_full(self) -> bool:
        return len(self._array) == self._capacity

    def is_empty(self) -> bool:
        return not self._array

    def enqueue(self, item: Any) -> int:
        if self.is_full():
            raise OverFlowError(self)

        self._array.append(item)
        self._rear += 1
        return 0

    def dequeue(self) -> Any:
        if self.is_empty() or self._front >= self._rear:
            raise UnderFlowError(self)
        deleted_item = self._array[self._front]
        self._front += 1
        return deleted_item

    def peek(self) -> Any:
        if self.is_empty() or self._front >= self._rear:
            return "QUEUE EMPTY"
        return self._array[self._front]

x = Queue()
x.enqueue(10)
x.enqueue(20)
x.dequeue()
print(x)