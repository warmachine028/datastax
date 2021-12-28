# Queue implementation using LinkedLists
from __future__ import annotations

from sys import maxsize
from typing import Any, Optional

from datastax.errors import OverFlowError, UnderFlowError
from datastax.linkedlists.linked_list import LinkedList, Node


class Queue(LinkedList):
    def __init__(self, array: list[Any] = None, capacity: int = None):
        super().__init__()
        self._rear = 0
        if capacity is not None and capacity < 0:
            print("Capacity can't be negative"
                  "Setting unbounded capacity")
        self._capacity = capacity if capacity is not None and capacity > 0 else maxsize
        if array and array[0] is not None:
            for item in array[:self._capacity]:
                self.enqueue(item)
    
    def is_empty(self) -> bool:
        return self.head is None
    
    def is_full(self) -> bool:
        return self._rear == self._capacity
    
    def enqueue(self, data: Any) -> int:
        if self.is_full():
            raise OverFlowError(self)
        super().append(data)
        self._rear += 1
        return 0
    
    def dequeue(self) -> Any:
        if self.is_empty():
            raise UnderFlowError(self)
        # Dequeue Operation
        deleted_node = self.head
        deleted_item = deleted_node.data
        self._head = self.head.next
        self._rear -= 1
        return deleted_item
    
    def peek(self) -> str:
        if self.is_empty(): return "QUEUE EMPTY"
        return str(self._tail.data if self._tail else None)
    
    def append(self, data: Any) -> None:
        print("WARNING: Method not available here.")
    
    def insert(self, data: Any) -> None:
        print("WARNING: Method not implemented here."
              "Please use enqueue method to insert")
    
    def __str__(self, head: Node = None):
        def maximum_breadth(ref: Optional[Node]) -> int:
            result = 0
            while ref:
                result = max(len(str(ref.data)), result)
                ref = ref.next
            return result
        
        if self.is_empty(): return '╔═══════════════════╗\n' \
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
            upper_part += f"╔{'═' * max_breadth}╗   "
            middle_part += f'║{str(item).center(max_breadth)}║ <-'
            lower_part += f"╚{'═' * max_breadth}╝   "
            temp = temp.next
        upper_part = f"{upper_part[:-1]}\n"
        middle_part += ' REAR\n'
        lower_part = f"{lower_part[:-1]}\n"
        
        return upper_part + middle_part + lower_part
