from __future__ import annotations

from typing import Any, Optional

from datastax.linkedlists.linked_list import Node, LinkedList


class DoublyNode(Node):
    def __init__(self, data: Any, nex: DoublyNode = None, prev: DoublyNode = None):
        super().__init__(data)
        self.next = nex
        self.prev = prev
    
    def __str__(self):
        return (f'Node[{self.prev.data}]' if self.prev else "NULL") + \
               f' ⟺ Node[{self.data}] ⟺ ' + \
               (f'Node[{self.next.data}]' if self.next else "NULL")


class DoublyLinkedList(LinkedList):
    def __init__(self, array: list[Any], head: DoublyNode = None):
        self._head: Optional[DoublyNode] = head
        self._tail = head
        super().__init__(array, head)
    
    def append(self, data) -> None:
        node = DoublyNode(data, None, self.tail)
        if not self.head: self._head = node
        else: self.tail.next = node
        self._tail = node
    
    def insert(self, data: Any):
        node = DoublyNode(data, self.head)
        if self.head: self.head.prev = node
        if not self.tail: self._tail = node
        self._head = node
    
    def __str__(self, reverse=False, node: DoublyNode = None):
        string = "NULL"
        if not self.head: return string
        head = node or (self.tail if reverse else self.head)
        while head:
            string += f" <-> Node[{head.data}]"
            head = head.prev if reverse else head.next
        string += " <-> NULL"
        return string
