# Queue Implementation using Lists (Pseudo Arrays)
import math
from typing import Any, Union

from datastax.errors import OverFlowError, UnderFlowError


class Queue:
    def __init__(self, capacity: int = None):
        self._capacity = capacity if capacity is not None else math.inf
        self._array: list[Any] = []
        self._front = self._rear = 0

    @property
    def array(self) -> list[Any]:
        return self._array[self._front:self._rear]

    @property
    def front(self) -> int:
        return self._front

    @property
    def rear(self) -> int:
        return self._rear

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

    def dequeue(self) -> Union[int, Any]:
        if self.is_empty() or self._front >= self._rear:
            raise UnderFlowError(self)
        deleted_item = self._array[self._front]
        self._front += 1
        return deleted_item

    def peek(self) -> Any:
        if self.is_empty() or self._front >= self._rear:
            return "QUEUE EMPTY"
        return self._array[self._front]

    # private method to mangle string __repr__
    @staticmethod
    def _mangled(item: Any) -> str:
        if '\n' in str(item):
            return f"{str(type(item))[8:-2].split('.')[-1]}@{id(item)}"
        return str(item)

    def __str__(self):
        if self.is_empty():
            return '┌───────────────────┐\n' \
                   '│    QUEUE EMPTY    │\n' \
                   '└───────────────────┘'
        padding = 4
        max_breadth = max(
            len((self._mangled(item))) for item in self._array
        ) + padding
        middle_part = 'FRONT -> │'
        upper_part = f"\n{' ' * (len(middle_part) - 1)}┌"
        lower_part = f"{' ' * (len(middle_part) - 1)}└"
        if self._front:  # Representing Garbage Values with '╳'
            for _ in self._array[:self._front]:
                middle_part += f"{'╳'.center(max_breadth)}│"
                upper_part += f"{'─' * max_breadth}┬"
                lower_part += f"{'─' * max_breadth}┴"
            upper_part = upper_part[:-1] + '╥'
            middle_part = middle_part[:-1] + '║'
            lower_part = lower_part[:-1] + '╨'
        for item in self._array[self._front:]:
            middle_part += f'{self._mangled(item).center(max_breadth)}│'
            upper_part += f"{'─' * max_breadth}┬"
            lower_part += f"{'─' * max_breadth}┴"
        upper_part = f"{upper_part[:-1]}"
        lower_part = f"{lower_part[:-1]}"
        upper_part += f"{'╖' if len(self._array) == self._front else '┐'}\n"
        middle_part += ' <- REAR\n'
        lower_part += f"{'╜' if len(self._array) == self._front else '┘'}\n"
        return upper_part + middle_part + lower_part

    def __repr__(self):
        return self.__str__()
