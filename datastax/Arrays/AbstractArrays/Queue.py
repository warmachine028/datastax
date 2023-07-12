from abc import ABC as AbstractClass, abstractmethod
from typing import Any
from datastax.Utils import Commons
from datastax.Arrays.AbstractArrays.Array import Array


class Queue(Array, AbstractClass):
    _rear = 0
    _front = 0

    def append(self, data: Any) -> None:
        raise NotImplementedError

    def insert(self, data: Any) -> None:
        raise NotImplementedError

    def pop(self) -> Any:
        raise NotImplementedError

    @property
    def front(self) -> int:
        return self._front

    @property
    def array(self) -> list[Any]:
        return self._array[self.front:self.rear] if self._array else []

    @property
    def rear(self) -> int:
        return self._rear

    def __str__(self):
        if self.is_empty():
            return '┌───────────────────┐\n' \
                   '│    QUEUE EMPTY    │\n' \
                   '└───────────────────┘'
        padding = 4
        max_breadth = max(
            len((Commons.repr(item))) for item in self.array
        ) + padding
        middle_part = 'FRONT -> │'
        upper_part = f"\n{' ' * (len(middle_part) - 1)}┌"
        lower_part = f"{' ' * (len(middle_part) - 1)}└"
        if self.front:  # Representing Garbage Values with '╳'
            for _ in self._array[:self.front]:
                middle_part += f"{'╳'.center(max_breadth)}│"
                upper_part += f"{'─' * max_breadth}┬"
                lower_part += f"{'─' * max_breadth}┴"
            upper_part = upper_part[:-1] + '╥'
            middle_part = middle_part[:-1] + '║'
            lower_part = lower_part[:-1] + '╨'
        for item in self._array[self.front:]:
            middle_part += f'{Commons.repr(item).center(max_breadth)}│'
            upper_part += f"{'─' * max_breadth}┬"
            lower_part += f"{'─' * max_breadth}┴"
        upper_part = f"{upper_part[:-1]}"
        lower_part = f"{lower_part[:-1]}"
        upper_part += f"{'╖' if len(self._array) == self.front else '┐'}\n"
        middle_part += ' <- REAR\n'
        lower_part += f"{'╜' if len(self._array) == self.front else '┘'}\n"
        return upper_part + middle_part + lower_part

    @abstractmethod
    def is_empty(self) -> bool:
        ...

    @abstractmethod
    def is_full(self) -> bool:
        ...

    @abstractmethod
    def enqueue(self, item: Any) -> int:
        ...

    @abstractmethod
    def dequeue(self) -> Any:
        ...

    @abstractmethod
    def peek(self) -> Any:
        ...
