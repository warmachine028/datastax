# Stack Implementation using Lists (Pseudo Arrays)
import math
from typing import Any

from datastax.errors import UnderFlowError, OverFlowError
from datastax.Arrays.AbstractArrays import Stack as AbstractStack


class Stack(AbstractStack):
    def __init__(self, *, capacity: int = None):
        self.set_capacity(capacity)

    @property
    def array(self) -> list[Any]:
        return self._array

    def is_full(self) -> bool:
        return len(self._array) == self.capacity

    def is_empty(self) -> bool:
        return not len(self._array)

    def push(self, item: Any) -> int:
        if self.is_full():  # Overflow Condition
            raise OverFlowError(self)

        self._array.append(item)
        return 0

    def pop(self) -> Any:
        if self.is_empty():  # Underflow Condition handled
            raise UnderFlowError(self)
        return self._array.pop()

    def __len__(self):
        return len(self._array)

    def peek(self) -> Any:
        return 'STACK EMPTY' if self.is_empty() else self._array[-1]
