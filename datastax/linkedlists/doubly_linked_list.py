from __future__ import annotations

from typing import Any, Optional

from datastax.linkedlists.private_lists import doubly_linked_list
from datastax.linkedlists.private_lists.doubly_linked_list import DoublyNode


class DoublyLinkedList(doubly_linked_list.DoublyLinkedList):
    def _construct(self, array: Optional[list[Any]]) -> DoublyLinkedList:
        if array and array[0] is not None:
            for item in array:
                self.append(item)
        return self

    def append(self, data) -> None:
        node = DoublyNode(data, None, self.tail)
        if not self.head:
            self._head = node
        else:
            self.tail.next = node
        self._tail = node

    def insert(self, data: Any):
        node = DoublyNode(data, self.head)
        if self.head:
            self.head.prev = node
        if not self.tail:
            self._tail = node
        self._head = node


if __name__ == '__main__':
    x = DoublyNode('one', DoublyNode(20), DoublyNode(30))
    y = DoublyNode('two', DoublyNode(20))
    z = DoublyNode('three', None, DoublyNode(20))
    a = DoublyNode('four')
    print(x,
          y,
          z,
          a, sep='\n')
    print_test_cases = [
        None,
        [1],
        [{1, 2, 3}, 1],
        [1, 'B', "C"],
        [[1, 2, 3], [1], 4],

    ]
    for item in print_test_cases:
        ll = DoublyLinkedList(item)
        print(ll)
        print(ll.head)
