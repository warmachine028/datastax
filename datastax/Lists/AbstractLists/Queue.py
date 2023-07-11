from abc import ABC, abstractmethod
from typing import Optional
from datastax.Lists.AbstractLists.LinkedList import LinkedList
from datastax.Lists.AbstractLists.Node import Node


class Queue(LinkedList, ABC):
    _capacity = 0
    _rear = 0

    @property
    def capacity(self):
        return self._capacity

    def __str__(self, head: Optional[Node] = None):
        def maximum_breadth(ref: Optional[Node]) -> int:
            result = 0
            while ref:
                result = max(len(str(ref.data)), result)
                ref = ref.next
            return result

        if self.is_empty():
            return '╔═══════════════════╗\n' \
                   '║    QUEUE EMPTY    ║\n' \
                   '╚═══════════════════╝'
        padding = 4
        max_breadth = maximum_breadth(self.head) + padding
        middle_part = 'FRONT -> '
        upper_part = f"{' ' * (len(middle_part) - 1)} "
        lower_part = f"{' ' * (len(middle_part) - 1)} "
        temp = self.head
        while temp:
            item = temp.data
            upper_part += f"┌{'─' * max_breadth}┐   "
            middle_part += f'|{str(item).center(max_breadth)}│ <-'
            lower_part += f"└{'─' * max_breadth}┘   "
            temp = temp.next
        upper_part = f"{upper_part[:-1]}\n"
        middle_part += ' REAR\n'
        lower_part = f"{lower_part[:-1]}\n"

        return upper_part + middle_part + lower_part

    @abstractmethod
    def is_empty(self):
        ...

    @abstractmethod
    def is_full(self):
        ...
