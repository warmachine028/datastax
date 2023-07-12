# Queue Implementation using Lists (Pseudo Arrays)
from typing import Any, Optional

from datastax.errors import OverFlowError, UnderFlowError
from datastax.Arrays.AbstractArrays import Queue as AbstractQueue


class Queue(AbstractQueue):
    def __init__(self, *, capacity: Optional[int] = None):
        self._array = []
        self.set_capacity(capacity)

    def is_full(self) -> bool:
        return len(self.array) == self.capacity

    def is_empty(self) -> bool:
        return not self.array

    def enqueue(self, item: Any) -> int:
        if self.is_full():
            raise OverFlowError(self)

        self._array.append(item)
        self._rear += 1
        return 0

    def dequeue(self) -> Any:
        if self.is_empty() or self.front >= self.rear:
            raise UnderFlowError(self)
        deleted_item = self._array[self.front]
        self._front += 1
        return deleted_item

    def __len__(self):
        return len(self.array)

    def peek(self) -> Any:
        if self.is_empty() or self._front >= self._rear:
            return "QUEUE EMPTY"
        return self._array[self.front]
