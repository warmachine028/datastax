# Queue Implementation using Lists (Pseudo Arrays)
import math
from typing import Any, Union


class Queue:
    def __init__(self, capacity: int = None):
        self._capacity = capacity if capacity is not None else math.inf
        self._array: list[Any] = []
        self._front = self._rear = 0
    
    @property
    def array_repr(self) -> list[Any]:
        return self._array[self._front:self._rear]
    
    def is_full(self) -> bool:
        return len(self._array) == self._capacity
    
    def is_empty(self) -> bool:
        return not len(self._array)
    
    def enqueue(self, item: Any) -> int:
        if self.is_full():
            print("WARNING: THE QUEUE IS ALREADY FULL, CANT ENQUEUE ANY FURTHER")
            return -1
        self._array.append(item)
        self._rear += 1
        return 0
    
    def dequeue(self) -> Union[int, Any]:
        if self.is_empty() or self._front >= self._rear:
            print("WARNING: THE QUEUE IS ALREADY EMPTY, CANT DEQUEUE ANY FURTHER")
            return -1
        deleted_item = self._array[self._front]
        self._front += 1
        return deleted_item
    
    def peek(self) -> str:
        if self.is_empty() or self._front >= self._rear: return "QUEUE EMPTY"
        return str(self._array[self._front])
    
    def __str__(self):
        if self.is_empty(): return '┌───────────────────┐\n' \
                                   '│    QUEUE EMPTY    │\n' \
                                   '└───────────────────┘'
        padding = 4
        max_breadth = max(len(str(item)) for item in self._array) + padding
        middle_part = 'FRONT -> │'
        upper_part = f"{' ' * (len(middle_part) - 1)}┌"
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
            middle_part += f'{str(item).center(max_breadth)}│'
            upper_part += f"{'─' * max_breadth}┬"
            lower_part += f"{'─' * max_breadth}┴"
        upper_part = f"{upper_part[:-1]}{'╖' if len(self._array) == self._front else '┐'}\n"
        middle_part += ' <- REAR\n'
        lower_part = f"{lower_part[:-1]}{'╜' if len(self._array) == self._front else '┘'}\n"
        return upper_part + middle_part + lower_part
    
    def __repr__(self):
        return self.__str__()
