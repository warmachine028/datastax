import unittest
from typing import Optional, Any

from datastax.Lists import DoublyCircularList
from datastax.Nodes import DoublyNode


class TestDoublyCircularList(unittest.TestCase):

    def setUp(self) -> None:
        self.dc_linkedList = DoublyCircularList()

    def test_append(self):
        # testing appending
        for i in range(1, 6):
            self.dc_linkedList.append(i)
        self.assertEqual([*range(1, 6)], self.items_in())
        self.assertEqual([*range(1, 6)][::-1], self.items_from_tail())

        # testing insert after appending
        self.dc_linkedList.insert(9)
        self.assertEqual([9, *range(1, 6)], self.items_in())
        self.assertEqual([9, *range(1, 6)][::-1], self.items_from_tail())

        # Testing circular traversal after above operation
        self.assertEqual([*range(1, 6), 9],
                         self.traverse_from(self.dc_linkedList.head.next))

    def test_building_from_existing_node(self):
        # Using this feature to merge 2 circular linked Lists
        existing_linked_list = DoublyCircularList([*range(10)])
        previous_tail = existing_linked_list.tail.prev
        ll = DoublyCircularList([*range(10, 20)], existing_linked_list.tail)
        # **MUST MANUALLY SET tail.next and head prev**
        ll.tail.set_next(existing_linked_list.head)
        ll.head.set_prev(previous_tail)
        # might be able to construct
        self.assertEqual([*range(20)], self.items_in(existing_linked_list))
        # but the tail of existing_linked_list will remain same
        self.assertNotEqual(existing_linked_list.tail, ll.tail)

        # the tail must be manually updated
        existing_linked_list.head.set_prev(ll.tail)
        existing_linked_list.set_tail(ll.tail)
        self.assertEqual(existing_linked_list.tail, ll.tail)
        self.assertEqual([*range(20)][::-1], self.items_from_tail(
            existing_linked_list))

        # Testing circular traversal after above operation
        self.assertEqual([*range(2, 20), 0, 1],
                         self.traverse_from(
                             existing_linked_list.head.next.next))

        # Testing build with an arbitrary node
        head = DoublyNode(7)
        cll = DoublyCircularList([1, 2, 3, 4, 5, 6], head)
        self.assertEqual([7, 1, 2, 3, 4, 5, 6], self.items_in(cll))
        self.assertEqual([7, 1, 2, 3, 4, 5, 6][::-1],
                         self.items_from_tail(cll))

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
            [[None], None, None],
            [[None, 1, 2, 3, 4, 5], None, 5],
            [[], None, None],
        ]
        for item, result in zip(items, results):
            ll = DoublyCircularList(item)
            # checking linkedlist items
            self.assertEqual(result[0], self.items_in(ll))
            # checking head
            self.assertEqual(result[1], ll.head.data if ll.head else None)
            # checking tail
            self.assertEqual(result[2], ll.tail.data if ll.tail else None)

    def test_insert(self):
        # testing inserting
        for i in range(1, 6):
            self.dc_linkedList.insert(i)
        self.assertEqual([*range(5, 0, -1)], self.items_in())
        # testing append after inserting
        self.dc_linkedList.append(9)
        self.assertEqual([*range(5, 0, -1), 9], self.items_in())

        # Testing circular traversal after above operation
        self.assertEqual([*range(4, 0, -1), 9, 5],
                         self.traverse_from(self.dc_linkedList.head.next))

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
            DoublyCircularList([1, 2]).head,  # -> Node
            DoublyCircularList([1, 2]),  # ->  self referential type
            None  # -> * can't be inserted as first item but otherwise okay...
            # entire list will be discarded if Node as first element
        ]
        for item in items:
            self.dc_linkedList.append(item)

        self.assertEqual(items, self.items_in())
        # Testing circular traversal after above operation
        self.assertEqual([*items[1:], items[0]],
                         self.traverse_from(self.dc_linkedList.head.next))

    def test_circular_traversal(self):
        items = [1, 2, 3, 4, 5]
        cll = DoublyCircularList(items)
        head = cll.head
        for i in range(len(items)):
            self.assertEqual(items[i:] + items[0:i], self.traverse_from(head))
            head = head.next

    def items_in(self, c_linked_list: DoublyCircularList = None
                 ) -> list[Optional[Any]]:
        if c_linked_list is None:
            c_linked_list = self.dc_linkedList
        result: list[Optional[Any]] = []
        head = c_linked_list.head
        while head:
            # for i in range(22):
            result.append(head.data)
            head = head.next
            if head is c_linked_list.head:
                break
        return result

    def items_from_tail(self, dc_linked_list: DoublyCircularList = None
                        ) -> list[Optional[Any]]:
        if dc_linked_list is None:
            dc_linked_list = self.dc_linkedList
        result: list[Optional[Any]] = []
        tail = dc_linked_list.tail
        while tail:
            # for i in range(21):
            result.append(tail.data)
            tail = tail.prev
            if tail is dc_linked_list.tail:
                break
        return result

    @staticmethod
    def traverse_from(head: DoublyNode) -> list[Optional[Any]]:
        result: list[Optional[Any]] = []
        ref: Optional[DoublyNode] = head
        while ref:
            result.append(ref.data)
            ref = ref.next
            if ref is head:
                break
        return result


if __name__ == '__main__':
    unittest.main()
    DCLL = DoublyCircularList([1, 2, 3])
