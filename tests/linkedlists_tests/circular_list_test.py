import unittest
from typing import Optional, Any

from datastax.linkedlists import CircularLinkedList, Node


class TestCircularLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.c_linkedList = CircularLinkedList()

    def test_append(self):
        # testing appending
        for i in range(1, 6):
            self.c_linkedList.append(i)
        self.assertEqual([*range(1, 6)], self.items_in())
        # testing insert after appending
        self.c_linkedList.insert(9)
        self.assertEqual([9, *range(1, 6)], self.items_in())

        # Testing circular traversal after above operation
        self.assertEqual([*range(1, 6), 9],
                         self.traverse_from(self.c_linkedList.head.next))

    def test_building_from_existing_node(self):
        # Using this feature to merge 2 circular linked Lists
        existing_linked_list = CircularLinkedList([*range(10)])
        ll = CircularLinkedList([*range(10, 20)], existing_linked_list.tail)
        # **MUST MANUALLY SET tail.next Pointer to old linked_list's head**
        ll.tail.next = existing_linked_list.head
        # might be able to construct
        self.assertEqual([*range(20)], self.items_in(existing_linked_list))
        # but the tail of existing_linked_list will remain same
        self.assertNotEqual(existing_linked_list.tail, ll.tail)

        # the tail must be manually updated
        existing_linked_list._tail = ll.tail
        self.assertEqual(existing_linked_list.tail, ll.tail)

        # Testing circular traversal after above operation
        self.assertEqual([*range(2, 20), 0, 1],
                         self.traverse_from(
                             existing_linked_list.head.next.next))

        # Testing build with an arbitrary node
        head = Node(7)
        cll = CircularLinkedList([1, 2, 3, 4, 5, 6], head)
        self.assertEqual([7, 1, 2, 3, 4, 5, 6], self.items_in(cll))

        # Testing circular traversal after above operation
        self.assertEqual([1, 2, 3, 4, 5, 6, 7],
                         self.traverse_from(cll.head.next))

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
            ll = CircularLinkedList(item)
            # checking linkedlist items
            self.assertEqual(result[0], self.items_in(ll))
            # checking head
            self.assertEqual(result[1], ll.head.data if ll.head else None)
            # checking tail
            self.assertEqual(result[2], ll.tail.data if ll.tail else None)

    def test_insert(self):
        # testing inserting
        for i in range(1, 6):
            self.c_linkedList.insert(i)
        self.assertEqual([*range(5, 0, -1)], self.items_in())
        # testing append after inserting
        self.c_linkedList.append(9)
        self.assertEqual([*range(5, 0, -1), 9], self.items_in())

        # Testing circular traversal after above operation
        self.assertEqual([*range(4, 0, -1), 9, 5],
                         self.traverse_from(self.c_linkedList.head.next))

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
            CircularLinkedList([1, 2]).head,  # -> Node
            CircularLinkedList([1, 2]),  # ->  self referential type
            None  # -> * can't be inserted as first item but otherwise okay...
            # entire list will be discarded if Node as first element
        ]
        for item in items:
            self.c_linkedList.append(item)

        self.assertEqual(items, self.items_in())
        # Testing circular traversal after above operation
        self.assertEqual([*items[1:], items[0]],
                         self.traverse_from(self.c_linkedList.head.next))

    def test_circular_traversal(self):
        items = [1, 2, 3, 4, 5]
        cll = CircularLinkedList(items)
        head = cll.head
        for i in range(len(items)):
            self.assertEqual(items[i:] + items[0:i], self.traverse_from(head))
            head = head.next

    def items_in(self, c_linked_list: CircularLinkedList = None
                 ) -> list[Optional[Any]]:
        if c_linked_list is None:
            c_linked_list = self.c_linkedList
        result: list[Optional[Any]] = []
        head = c_linked_list.head
        while head:
            result.append(head.data)
            head = head.next
            if head is c_linked_list.head:
                break
        return result

    @staticmethod
    def traverse_from(head: Node) -> list[Optional[Any]]:
        result: list[Optional[Any]] = []
        ref: Optional[Node] = head
        while ref:
            result.append(ref.data)
            ref = ref.next
            if ref is head:
                break
        return result


if __name__ == '__main__':
    unittest.main()
