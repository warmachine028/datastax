from __future__ import annotations

from typing import Any, Optional

from datastax.linkedlists.doubly_linked_list import DoublyLinkedList
from datastax.linkedlists.private_lists import doubly_circular_llist


class DoublyCircularList(doubly_circular_llist.DoublyCircularList,
                         DoublyLinkedList):

    def _construct(self, array: Optional[list[Any]]) -> DoublyCircularList:
        if array and array[0] is not None:
            for item in array:
                self.append(item)
        return self

    def append(self, data: Any) -> None:
        super().append(data)
        self.head.prev, self.tail.next = self.tail, self.head

    def insert(self, data: Any) -> None:
        super().insert(data)
        self.head.prev, self.tail.next = self.tail, self.head


if __name__ == '__main__':
    print_test_cases = [
        None,
        [1],
        [{1, 2, 3}, 1],
        [1, 'B', "C"],
        [[1, 2, 3], [1], 4],

    ]
    for item in print_test_cases:
        ll = DoublyCircularList(item)
        print(ll)
        print(ll.head)
