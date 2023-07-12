import unittest

from datastax.Lists.DoublyNode import DoublyNode
from datastax.Lists.Node import Node


class TestDoublyNode(unittest.TestCase):
    def setUp(self) -> None:
        self.test_cases = [
            None,
            [1],
            [{1, 2, 3}, 1],
            0,
            'A',
            DoublyNode(10),
            DoublyNode(10, prev=DoublyNode(100)),
            DoublyNode(10, DoublyNode(100)),
            DoublyNode(10, DoublyNode(100), DoublyNode(1000))
        ]

    def test_string_with_none(self):
        result = \
            '        ┌────╥────────╥────┐\n' \
            ' NULL <----  ║  None  ║  ---->  NULL\n' \
            '        └────╨────────╨────┘\n'

        self.assertEqual(result, DoublyNode(self.test_cases[0]).__str__())

    def test_string_with_list(self):
        result = \
            '        ┌────╥───────╥────┐\n' \
            ' NULL <----  ║  [1]  ║  ---->  NULL\n' \
            '        └────╨───────╨────┘\n'

        self.assertEqual(result, DoublyNode(self.test_cases[1]).__str__())

    def test_string_with_combination(self):
        result = \
            '        ┌────╥──────────────────╥────┐\n' \
            ' NULL <----  ║  [{1, 2, 3}, 1]  ║  ---->  NULL\n' \
            '        └────╨──────────────────╨────┘\n'

        self.assertEqual(result, DoublyNode(self.test_cases[2]).__str__())

    def test_string_with_0(self):
        result = \
            '        ┌────╥─────╥────┐\n' \
            ' NULL <----  ║  0  ║  ---->  NULL\n' \
            '        └────╨─────╨────┘\n'

        self.assertEqual(result, DoublyNode(self.test_cases[3]).__str__())

    def test_string_with_character(self):
        result = \
            '        ┌────╥─────╥────┐\n' \
            ' NULL <----  ║  A  ║  ---->  NULL\n' \
            '        └────╨─────╨────┘\n'

        self.assertEqual(result, DoublyNode(self.test_cases[4]).__str__())

    def test_string_with_self(self):
        node = self.test_cases[5]
        _id = id(node)
        self.assertIn(f"DoublyNode@{_id}", DoublyNode(node).__str__())

    def test_string_with_prev(self):
        result = \
            '        ┌────╥──────╥────┐\n' \
            ' prev <----  ║  10  ║  ---->  NULL\n' \
            '        └────╨──────╨────┘\n'

        self.assertEqual(result, self.test_cases[6].__str__())

    def test_string_with_next(self):
        result = \
            '        ┌────╥──────╥────┐\n' \
            ' NULL <----  ║  10  ║  ---->  next\n' \
            '        └────╨──────╨────┘\n'

        self.assertEqual(result, self.test_cases[7].__str__())

    def test_next_as_None(self):
        _next = None
        node = DoublyNode('data', _next)
        self.assertEqual(node.next, None)

    def test_next_as_NonDoublyNode(self):
        next_item = Node(10)
        self.assertRaises(TypeError, lambda: DoublyNode('data', next_item))

    def test_next_set_manually(self):
        next_item = DoublyNode(10)
        node = DoublyNode(100)
        node.set_next(next_item)
        self.assertEqual(node.next, next_item)

    def test_next_None_set_manually(self):
        next_item = None
        node = DoublyNode(100)
        node.set_next(next_item)
        self.assertEqual(node.next, None)

    def test_next_NonDoublyNode_set_manually(self):
        next_item = list()
        node = DoublyNode(100)
        self.assertRaises(TypeError, lambda: node.set_next(next_item))

    def test_prev_as_None(self):
        prev_item = None
        node = DoublyNode('data', prev=prev_item)
        self.assertEqual(node.prev, None)

    def test_prev_as_NonDoublyNode(self):
        prev_item = ['Non Node Item']
        self.assertRaises(
            TypeError,
            lambda: DoublyNode('data', prev=prev_item)
        )

    def test_prev_set_manually(self):
        prev_item = DoublyNode(10)
        node = DoublyNode(100)
        node.set_prev(prev_item)
        self.assertEqual(node.prev, prev_item)

    def test_prev_None_set_manually(self):
        prev_item = None
        node = DoublyNode(100)
        node.set_prev(prev_item)
        self.assertEqual(node.prev, None)

    def test_prev_NonDoublyNode_set_manually(self):
        prev_item = list()
        node = DoublyNode(100)
        self.assertRaises(TypeError, lambda: node.set_prev(prev_item))

    def test_prev_NonDoublyNode(self):
        prev_item = list()
        node = DoublyNode(100)
        self.assertRaises(TypeError, lambda: node.set_prev(prev_item))


if __name__ == '__main__':
    unittest.main()
