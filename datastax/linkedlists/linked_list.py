from __future__ import annotations

from typing import Any


class Node:
    def __init__(self, data: Any, nex: Node = None):
        self.data = data
        self.next = nex
    
    def __str__(self):
        return f'Node[{self.data}] -> ' \
               f"{f'Node[{self.next.data}]' if self.next else 'NULL'}"
    
    def __repr__(self):
        return self.__str__()


class LinkedList:
    def __init__(self, array: list[Any] = None, head: Node = None):
        self._head = head
        self._tail = head
        
        if array and array[0] is not None:
            for item in array: self.append(item)
    
    @property
    def head(self): return self._head
    
    @property
    def tail(self): return self._tail
    
    def append(self, data: Any) -> None:
        node = Node(data)
        if not self.head: self._head = node
        else: self.tail.next = node
        self._tail = node
    
    def insert(self, data: Any):
        node = Node(data, self.head)
        if not self.tail: self._tail = node
        self._head = node
    
    def __str__(self, head: Node = None):
        string = ""
        head = head or self.head
        while head:
            string += f"Node[{head.data}] -> "
            head = head.next
        string += "NULL"
        return string
    
    def __repr__(self):
        return self.__str__()
