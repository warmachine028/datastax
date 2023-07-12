from abc import ABC, abstractmethod
from typing import Optional, Any
from datastax.Lists.AbstractLists.LinkedList import LinkedList
from datastax.Lists.AbstractLists.Node import Node
from datastax.Utils import Commons


class Queue(LinkedList, ABC):
    _capacity = 0
    _rear = 0

    def append(self, data: Any) -> None:
        raise NotImplementedError

    def insert(self, data: Any) -> None:
        raise NotImplementedError

    @property
    def capacity(self):
        return self._capacity

    def __str__(self, head: Optional[Node] = None):
        if self.is_empty():
            return '╔═══════════════════╗\n' \
                   '║    QUEUE EMPTY    ║\n' \
                   '╚═══════════════════╝'
        padding = 4
        ref = self.head
        max_breadth = self._max_width(ref) + padding
        middle_part = 'FRONT -> '
        lower_part = upper_part = f"{' ' * (len(middle_part) - 1)} "
        while ref:
            item = ref.data
            upper_part += f"┌{'─' * max_breadth}┐   "
            middle_part += f'|{Commons.repr(item).center(max_breadth)}│ <-'
            lower_part += f"└{'─' * max_breadth}┘   "
            ref = ref.next
        upper_part = f"{upper_part[:-1]}\n"
        middle_part += ' REAR\n'
        lower_part = f"{lower_part[:-1]}\n"

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
    def peek(self) -> str | Optional[Any]:
        ...
