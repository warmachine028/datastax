from typing import Any, Optional, Iterable, Self

from datastax.Lists.DoublyNode import DoublyNode
from datastax.Lists.LinkedList import LinkedList
from datastax.Lists.AbstractLists import DoublyLinkedList as AbstractList


class DoublyLinkedList(AbstractList, LinkedList):
    def __init__(self, items: Optional[Iterable[Any]] = None,
                 head: Optional[DoublyNode] = None,
                 tail: Optional[DoublyNode] = None):
        if head and tail:
            head.set_next(tail)
            tail.set_prev(head)
        super().__init__(items, head, tail)

    def _construct(self, array: Iterable[Any]) -> Self:
        return super()._construct(array)

    def set_head(self, head):
        if head is not None and not isinstance(head, DoublyNode):
            raise TypeError("The 'head' parameter must be an "
                            "instance of DoublyNode or its subclass.")
        super().set_head(head)

    def set_tail(self, tail):
        if tail is not None and not isinstance(tail, DoublyNode):
            raise TypeError("The 'tail' parameter must be an "
                            "instance of DoublyNode or its subclass.")
        super().set_tail(tail)

    def append(self, data: Any) -> None:
        node = DoublyNode(data)
        if self.tail and not self.head:
            self.set_head(self.tail)
        if not self.head:
            self.set_head(node)
        else:
            node.set_prev(self.tail)
            self.tail.set_next(node)
        self.set_tail(node)

    def insert(self, data: Any):
        node = DoublyNode(data, self.head)
        if self.head:
            self.head.set_prev(node)
        if not self.tail:
            self.set_tail(node)
        self.set_head(node)
