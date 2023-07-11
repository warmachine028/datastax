import random
import unittest
from typing import Optional, Any

from datastax.Lists.DoublyLinkedList import DoublyLinkedList
from datastax.Lists.DoublyNode import DoublyNode


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.d_linkedList = DoublyLinkedList()
        self.print_test_cases = [
            None,
            [1],
            [{1, 2, 3}, 1],
            [1, 'B', "C"],
            [[1, 2, 3], [1], 4]
        ]

    def test_append(self):
        # testing appending
        for i in range(1, 6):
            self.d_linkedList.append(i)
        self.assertEqual([*range(1, 6)], self.items_in())
        self.assertEqual([*range(1, 6)][::-1], self.items_from_tail())

        # testing insert after appending
        self.d_linkedList.insert(9)
        self.assertEqual([9, *range(1, 6)], self.items_in())
        self.assertEqual([9, *range(1, 6)][::-1], self.items_from_tail())

    def test_building_from_existing_node(self):
        existing_linked_list = DoublyLinkedList([*range(10)])
        ll = DoublyLinkedList([*range(10, 20)], existing_linked_list.tail)

        # might be able to construct
        self.assertEqual([*range(20)], self.items_in(existing_linked_list))

        # but the tail of existing_linked_list will remain same
        self.assertNotEqual([*range(20)][::-1],
                            self.items_from_tail(existing_linked_list))
        self.assertNotEqual(existing_linked_list.tail, ll.tail)

        # the tail must be manually updated
        existing_linked_list._tail = ll.tail
        self.assertEqual(existing_linked_list.tail, ll.tail)
        self.assertEqual([*range(20)][::-1], self.items_from_tail(
            existing_linked_list))

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
            [[], None, None]
        ]
        for test_case, result in zip(items, results):
            dll = DoublyLinkedList(test_case)
            # checking doublyLinkedList items
            self.assertEqual(result[0], self.items_in(dll))
            # checking items from the end
            self.assertEqual(result[0][::-1], self.items_from_tail(dll))
            # checking head
            self.assertEqual(result[1], dll.head.data if dll.head else None)
            # checking tail
            self.assertEqual(result[2], dll.tail.data if dll.tail else None)

    def test_insert(self):
        # testing inserting
        for i in range(1, 6):
            self.d_linkedList.insert(i)
        self.assertEqual([[*range(5, 0, -1)], [*range(1, 6)]],
                         [self.items_in(), self.items_from_tail()])

        # testing append after inserting
        self.d_linkedList.append(9)
        self.assertEqual([[*range(5, 0, -1), 9], [9, *range(1, 6)]],
                         [self.items_in(), self.items_from_tail()])

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
            DoublyLinkedList([1, 2]).head,  # -> DoublyNode
            DoublyLinkedList([1, 2]),  # ->  self referential type
            None  # -> * can't be inserted as first item but otherwise okay...
            # entire list will be discarded if Node as first element
        ]
        for item in items:
            self.d_linkedList.append(item)

        self.assertEqual(items, self.items_in())
        self.assertEqual(items[::-1], self.items_from_tail())

    def test_iter(self):
        items = random.sample(range(100), 10)
        list_ = DoublyLinkedList(items)
        for list_item, actual_item in zip(items, list_):
            self.assertEqual(list_item, actual_item)

    def test_string(self):
        results = [
            '         \n NULL \n        \n',

            '               HEAD      \n'
            '               TAIL      \n'
            '         ┌────╥─────╥────┐  \n'
            ' NULL <-----  ║  1  ║  -----> NULL\n'
            '         └────╨─────╨────┘  \n',

            '                   HEAD                        TAIL          \n'
            '         ┌────╥─────────────╥────┐   ┌────╥─────────────╥────┐'
            '  \n'
            ' NULL <-----  ║  {1, 2, 3}  ║  <------->  ║      1      ║  ----->'
            ' NULL\n'
            '         └────╨─────────────╨────┘   └────╨─────────────╨────┘'
            '  \n',

            '               HEAD                                    TAIL    '
            '  \n'
            '         ┌────╥─────╥────┐   ┌────╥─────╥────┐   ┌────╥─────╥──'
            '──┐  \n'
            ' NULL <-----  ║  1  ║  <------->  ║  B  ║  <------->  ║  C  ║  '
            '-----> NULL\n'
            '         └────╨─────╨────┘   └────╨─────╨────┘   └────╨─────╨──'
            '──┘  \n',

            '                   HEAD                                        '
            '            TAIL          \n'
            '         ┌────╥─────────────╥────┐   ┌────╥─────────────╥────┐ '
            '  ┌────╥─────────────╥────┐  \n'
            ' NULL <-----  ║  [1, 2, 3]  ║  <------->  ║     [1]     ║  <---'
            '---->  ║      4      ║  -----> NULL\n'
            '         └────╨─────────────╨────┘   └────╨─────────────╨────┘ '
            '  └────╨─────────────╨────┘  \n'
        ]
        for testcase, result in zip(self.print_test_cases, results):
            list_ = DoublyLinkedList(testcase)
            self.assertEqual(result, list_.__str__())

    def test_construction_with_tail(self):
        items = [
            # <- Using general list of ints with DoublyNode tail
            ([1, 2, 3, 4, 5], DoublyNode(6)),
            # <- Using range object unpacking in list with DoublyNode tail
            ([*range(10)], DoublyNode(9)),
            # <- Using Empty list with None tail
            ([], None),
            # <- Using only None item passed through list with DoublyNode tail
            ([None], DoublyNode(None)),
            # <- Using First item as None with DoublyNode tail
            ([None, 1, 2, 3, 4], DoublyNode(5)),
            (None, None),  # <- Using None passed directly with None tail
        ]
        results = [
            [[6, 1, 2, 3, 4, 5], 6, 5],
            [[9, *range(10)], 9, 9],
            [[], None, None],
            [[None, None], None, None],
            [[5, None, 1, 2, 3, 4], 5, 4],
            [[], None, None]
        ]
        for test_case, result in zip(items, results):
            dll = DoublyLinkedList(test_case[0], tail=test_case[1])
            # checking linked list items
            self.assertEqual(result[0], self.items_in(dll))
            # checking items from the end
            self.assertEqual(result[0][::-1], self.items_from_tail(dll))
            # checking head
            self.assertEqual(result[1], dll.head.data if dll.head else None)
            # checking tail
            self.assertEqual(result[2], dll.tail.data if dll.tail else None)

    def test_construction_with_both(self):
        items = [
            # <- Using general list of ints with DoublyNode tail
            ([1, 2, 3, 4, 5], DoublyNode(6), DoublyNode(7)),
            ([*range(10)], DoublyNode(9),
             # <- Using range object unpacking in list with DoublyNode tail
             DoublyNode(19)),
            ([], None, DoublyNode(10)),  # <- Using Empty list with None tail
            # <- Using only None item passed through list with DoublyNode tail
            ([None], DoublyNode(None), DoublyNode(0)),
            # <- Using First item as None with DoublyNode tail
            ([None, 1, 2, 3, 4], DoublyNode(5), DoublyNode(10)),
            (None, None, None),  # <- Using None passed directly with None tail
        ]
        results = [
            [[6, 7, 1, 2, 3, 4, 5], 6, 5],
            [[9, 19, *range(10)], 9, 9],
            [[10], 10, 10],
            [[None, 0, None], None, None],
            [[5, 10, None, 1, 2, 3, 4], 5, 4],
            [[], None, None]
        ]
        for test_case, result in zip(items, results):
            dll = DoublyLinkedList(*test_case)
            # checking linked list items
            self.assertEqual(result[0], self.items_in(dll))
            # checking items from the end
            self.assertEqual(result[0][::-1], self.items_from_tail(dll))
            # checking head
            self.assertEqual(result[1], dll.head.data if dll.head else None)
            # checking tail
            self.assertEqual(result[2], dll.tail.data if dll.tail else None)

    def items_in(self, d_linked_list: DoublyLinkedList = None
                 ) -> list[Optional[Any]]:
        if d_linked_list is None:
            d_linked_list = self.d_linkedList
        result: list[Optional[Any]] = []
        head = d_linked_list.head
        while head:
            result.append(head.data)
            head = head.next
        return result

    def items_from_tail(self, d_linked_list: Optional[DoublyLinkedList] = None
                        ) -> list[Optional[Any]]:
        if d_linked_list is None:
            d_linked_list = self.d_linkedList
        result: list[Optional[Any]] = []
        tail = d_linked_list.tail
        while tail:
            result.append(tail.data)
            tail = tail.prev
        return result


if __name__ == '__main__':
    unittest.main()
