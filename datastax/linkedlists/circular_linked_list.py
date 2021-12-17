from __future__ import annotations

from typing import Any

from datastax.linkedlists.linked_list import Node, LinkedList


class CircularLinkedList(LinkedList):
    def append(self, data: Any) -> None:
        super().append(data)
        self.tail.next = self.head
    
    def insert(self, data: Any):
        super().insert(data)
        self.tail.next = self.head
    
    def __str__(self, node: Node = None):
        head = node or self.head
        if not head: return "NULL"
        string = f"┌->"
        ref = head
        while True:
            string += f' Node[{str(ref.data)}] ->'
            ref = ref.next
            if ref is head: break
        string += f"┐\n└{'<'.center(len(string) - 1, '─')}┘"
        return string
