# Stack Implementation using Lists (Pseudo Arrays)
import math
from typing import Any, Union

from datastax.errors import UnderFlowError, OverFlowError


class Stack:
    def __init__(self, capacity: int = None):
        self.capacity = capacity if capacity is not None else math.inf
        self._array: list[Any] = []

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

    def pop(self) -> Union[int, Any]:
        if self.is_empty():  # Underflow Condition handled
            raise UnderFlowError(self)

        return self._array.pop()

    def __len__(self):
        return len(self._array)

    def peek(self) -> str:
        return 'STACK EMPTY' if self.is_empty() else self._array[-1]

    # private method to mangle string __repr__
    @staticmethod
    def _mangled(item: Any) -> str:
        if '\n' in str(item):
            return f"{str(type(item))[8:-2].split('.')[-1]}@{id(item)}"
        return str(item)

    def __str__(self):
        if self.is_empty():
            return '│STACK EMPTY│\n' \
                   '╰───────────╯\n'
        padding = 9
        maximum_breadth = max(
            len((self._mangled(item))) for item in self._array
        ) + padding
        # For FULLY LOADED STACK
        if self.is_full():
            string = f"┌{'─' * maximum_breadth}┐\n"
        elif (len(self._array) < 0.7 * self.capacity) or (
                self.capacity - len(self._array) > 5):
            string = (
                f"│{' ' * maximum_breadth}│\n"
                f":{' ' * maximum_breadth}:\n"
            )  # Shrink visualization
        else:
            string = f"│{' ' * maximum_breadth}│\n" * 2 * (
                    self.capacity - len(self._array))  # Expand Visualization

        for n, item in enumerate(self._array[::-1]):
            top = (
                '' if self.is_full() and not n
                else f"├{'─' * maximum_breadth}┤\n"
            )
            bottom = (
                f"│{self._mangled(item).center(maximum_breadth)}│"
                f"{' <- TOP' if not n else ''}\n"
            )
            string += top + bottom
        string += f"╰{'─' * maximum_breadth}╯\n"
        return string

    def __repr__(self):
        return self.__str__()
