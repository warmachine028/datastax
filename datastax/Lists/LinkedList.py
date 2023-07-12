from typing import Any, Optional, Iterable, Self

from datastax.Lists.Node import Node
from datastax.Lists.AbstractLists import LinkedList as AbstractLinkedList


class LinkedList(AbstractLinkedList):
    def __init__(
            self,
            items: Optional[Iterable[Any]] = None,
            head: Optional[Node] = None,
            tail: Optional[Node] = None
    ):
        if head and tail:
            head.set_next(tail)
        self.set_head(head)
        self.set_tail(tail)
        if tail and not head:
            self.set_head(tail)
        self._construct(items if items else [])

    def __iter__(self):
        ref = self._head
        while ref:
            yield ref.data
            ref = ref.next

    def set_head(self, head: Node | None):
        if head is None or isinstance(head, Node):
            self._head = head
            return
        raise TypeError("The 'head' parameter must be an "
                        "instance of Node or its subclass.")

    def set_tail(self, tail: Node | None):
        if tail is None or isinstance(tail, Node):
            self._tail = tail or self.head
            return
        raise TypeError("The 'tail' parameter must be an "
                        "instance of Node or its subclass.")

    def _construct(self, items: Iterable[Any]) -> Self:
        for item in items:
            self.append(item)
        return self

    def append(self, data: Any) -> None:
        node = Node(data)
        if self.tail and not self.head:
            self.set_head(self.tail)
        if not self.head:
            self.set_head(node)
        else:
            self.tail.set_next(node)
        self.set_tail(node)

    def insert(self, data: Any) -> None:
        node = Node(data, self.head)
        if not self.tail:
            self.set_tail(node)
        self.set_head(node)
