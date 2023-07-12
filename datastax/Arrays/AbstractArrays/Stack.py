from abc import ABC as AbstractClass, abstractmethod
from typing import Any
from datastax.Utils import Commons
from datastax.Arrays.AbstractArrays.Array import Array


class Stack(Array, AbstractClass):
    def append(self, data: Any) -> None:
        raise NotImplementedError

    @property
    def array(self) -> list[Any]:
        return self._array

    def insert(self, data: Any) -> None:
        raise NotImplementedError

    def __str__(self):
        if self.is_empty():
            return '│STACK EMPTY│\n' \
                   '╰───────────╯\n'
        padding = 9
        maximum_breadth = max(
            len((Commons.repr(item))) for item in self._array
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
                f"│{Commons.repr(item).center(maximum_breadth)}│"
                f"{' <- TOP' if not n else ''}\n"
            )
            string += top + bottom
        string += f"╰{'─' * maximum_breadth}╯\n"
        return string

    @abstractmethod
    def is_empty(self) -> bool:
        ...

    @abstractmethod
    def is_full(self) -> bool:
        ...

    @abstractmethod
    def peek(self) -> Any:
        ...
