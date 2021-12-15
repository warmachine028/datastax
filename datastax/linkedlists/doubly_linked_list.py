from __future__ import annotations

from typing import Any

from datastax.linkedlists.linked_list import Node, LinkedList


class DoublyNode(Node):
    def __init__(self, data: Any, nex: Node = None, prev=None):
        super().__init__(data, nex)
        self.prev = prev
    
    def __str__(self):
        return (f'Node[{self.prev.data}]' if self.prev else "NULL") + \
               f' ⟺ Node[{self.data}] ⟺ ' + \
               (f'Node[{self.next.data}]' if self.next else "NULL")


class DoublyLinkedList(LinkedList):
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
        node = node or (self.tail if reverse else self.head)
        while node:
            string += f" <-> Node[{node.data}]"
            node = node.prev if reverse else node.next
        string += " <-> NULL"
        return string


# __main__
if __name__ == '__main__':
    D = DoublyLinkedList([*range(5)])
    print("head -> ", D.head)
    D.insert(10)
    D.insert(20)
    D.append(199)
    print(D)
    print(D.__str__(True))
