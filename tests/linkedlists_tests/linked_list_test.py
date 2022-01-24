import unittest
from typing import Optional, Any

from datastax.linkedlists import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.linkedList = LinkedList()

    def test_append(self):
        # testing appending
        for i in range(1, 6):
            self.linkedList.append(i)
        self.assertEqual([*range(1, 6)], self.items_in())

        # testing insert after appending
        self.linkedList.insert(9)
        self.assertEqual([9, *range(1, 6)], self.items_in())

    def test_building_from_existing_node(self):
        existing_linked_list = LinkedList([*range(10)])
        ll = LinkedList([*range(10, 20)], existing_linked_list.tail)

        # might be able to construct
        self.assertEqual([*range(20)], self.items_in(existing_linked_list))

        # but the tail of existing_linked_list will remain same
        self.assertNotEqual(existing_linked_list.tail, ll.tail)
        # the tail must be manually updated
        existing_linked_list._tail = ll.tail
        self.assertEqual(existing_linked_list.tail, ll.tail)

    def test_construction(self):
        items = [
            [1, 2, 3, 4, 5, 6],  # <- Using general list of ints
            [*range(10)],  # <- Using range object unpacking in list
            [],  # <- Using Empty list
            [None],  # <- Using only None item passed through list
            [None, 1, 2, 3, 4, 5],  # <- Using First item as None
            None,  # <- Using None passed directly
        ]
        results = [
            [[1, 2, 3, 4, 5, 6], 1, 6],
            [[*range(10)], 0, 9],
            [[], None, None],
            [[], None, None],
            [[], None, None],
            [[], None, None]
        ]
        for item, result in zip(items, results):
            ll = LinkedList(item)
            # checking linkedlist items
            self.assertEqual(result[0], self.items_in(ll))
            # checking head
            self.assertEqual(result[1], ll.head.data if ll.head else None)
            # checking tail
            self.assertEqual(result[2], ll.tail.data if ll.tail else None)

    def test_insert(self):
        # testing inserting
        for i in range(1, 6):
            self.linkedList.insert(i)
        self.assertEqual([*range(5, 0, -1)], self.items_in())
        # testing append after inserting
        self.linkedList.append(9)
        self.assertEqual([*range(5, 0, -1), 9], self.items_in())

    def test_inserting_heterogeneous_items(self):
        # inserting miscellaneous items
        items = [
            {1: 2, 2: 3, 3: 4},  # -> dictionary
            {1, 2, 3, 4, 5, 6, 7},  # -> set
            [1, 2, 3, 4, 5],  # -> list
            1234567890,  # -> integer
            "string",  # -> string
            'A',  # -> char
            # Inserting Uncommon items
            LinkedList([1, 2]).head,  # -> Node
            LinkedList([1, 2]),  # ->  self referential type
            None  # -> * can't be inserted as first item but otherwise okay...
            # entire list will be discarded if Node as first element
        ]
        for item in items:
            self.linkedList.append(item)

        self.assertEqual(items, self.items_in())

    def items_in(self, linked_list: LinkedList = None) -> list[Optional[Any]]:
        if linked_list is None:
            linked_list = self.linkedList
        result: list[Optional[Any]] = []
        head = linked_list.head
        while head:
            result.append(head.data)
            head = head.next
        return result


if __name__ == '__main__':
    unittest.main()
