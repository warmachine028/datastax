from __future__ import annotations

from typing import Any


class Node:
    def __init__(self, data, nex: Node = None):
        self.data = data
        self.next = nex


class LinkedList:
    def __init__(self, array: list[Any] = None, head: Node = None):
        self._head = head
        self._tail = head
        
        if array and array[0]:
            for item in array: self.append(item)
    
    @property
    def head(self): return self._head
    
    @property
    def tail(self): return self._tail
    
    def append(self, data: Any) -> None:
        node = Node(data)
        if not self.head: self._head = node
        else: self._tail.next = node
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


# __main__
if __name__ == '__main__':
    LL = LinkedList()
    print(LL)
    LL.insert(10)
    LL.insert(11)
    LL.append(90)
    LL.insert(199)
    LL.append(109)
    print(LL)
