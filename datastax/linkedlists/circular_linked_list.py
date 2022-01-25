from __future__ import annotations

from typing import Any, Optional

from datastax.linkedlists.linked_list import LinkedList
from datastax.linkedlists.private_lists import circular_linked_list


class CircularLinkedList(circular_linked_list.CircularLinkedList,
                         LinkedList):
    def _construct(self, array: Optional[list[Any]]) -> CircularLinkedList:
        if array and array[0] is not None:
            for item in array:
                self.append(item)
        return self

    def append(self, data: Any) -> None:
        super().append(data)
        self.tail.next = self.head

    def insert(self, data: Any):
        super().insert(data)
        self.tail.next = self.head


if __name__ == '__main__':
    print_test_cases = [
        None,
        [1],
        [{1, 2, 3}, 1],
        [1, 'B', "C"],
        [[1, 2, 3], [1], 4],
    ]
    for item in print_test_cases:
        ll = CircularLinkedList(item)
        print(ll)
        print(ll.head)
