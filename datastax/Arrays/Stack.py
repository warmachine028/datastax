# Stack Implementation using Lists (Pseudo Arrays)
from typing import Any, Optional

from datastax.errors import UnderFlowError, OverFlowError
from datastax.Arrays.AbstractArrays import Stack as AbstractStack


class Stack(AbstractStack):
    def __init__(self, *, capacity: Optional[int] = None):
        self._array = []
        self.set_capacity(capacity)

    def is_full(self) -> bool:
        return len(self.array) == self.capacity

    def is_empty(self) -> bool:
        return not self.array

    def push(self, item: Any) -> int:
        if self.is_full():  # Overflow Condition
            raise OverFlowError(self)

        self.array.append(item)
        return 0

    def pop(self) -> Any:
        if self.is_empty():  # Underflow Condition handled
            raise UnderFlowError(self)
        return self.array.pop()

    def __len__(self):
        return len(self.array)

    def peek(self) -> Any:
        return 'STACK EMPTY' if self.is_empty() else self.array[-1]
