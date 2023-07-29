import unittest

from datastax.Nodes import Node


class TestNode(unittest.TestCase):
    def setUp(self) -> None:
        self.test_cases = [
            None,
            [1],
            [{1, 2, 3}, 1],
            0,
            'A',
            Node(10)
        ]

    def test_string_with_none(self):
        result = \
            ' ┌────────╥────┐\n' \
            ' │  None  ║ ------> NULL\n' \
            ' └────────╨────┘\n'

        self.assertEqual(result, Node(self.test_cases[0]).__str__())

    def test_string_with_list(self):
        result = \
            ' ┌───────╥────┐\n' \
            ' │  [1]  ║ ------> NULL\n' \
            ' └───────╨────┘\n'

        self.assertEqual(result, Node(self.test_cases[1]).__str__())

    def test_string_with_combination(self):
        result = \
            ' ┌──────────────────╥────┐\n' \
            ' │  [{1, 2, 3}, 1]  ║ ------> NULL\n' \
            ' └──────────────────╨────┘\n'

        self.assertEqual(result, Node(self.test_cases[2]).__str__())

    def test_string_with_0(self):
        result = \
            ' ┌─────╥────┐\n' \
            ' │  0  ║ ------> NULL\n' \
            ' └─────╨────┘\n'

        self.assertEqual(result, Node(self.test_cases[3]).__str__())

    def test_string_with_character(self):
        result = \
            ' ┌─────╥────┐\n' \
            ' │  A  ║ ------> NULL\n' \
            ' └─────╨────┘\n'

        self.assertEqual(result, Node(self.test_cases[4]).__str__())

    def test_string_with_self(self):
        node = self.test_cases[5]
        _id = id(node)
        self.assertIn(f"Node@{_id}", Node(node).__str__())

    def test_next_passed_as_argument(self):
        _next = Node('nextData')
        node = Node('data', _next)
        self.assertEqual(node.next, _next)

    def test_next_as_None(self):
        _next = None
        node = Node('data', _next)
        self.assertEqual(node.next, None)

    def test_next_as_NonNode(self):
        next_item = ['Non Node Item']
        self.assertRaises(TypeError, lambda: Node('data', next_item))

    def test_next_set_manually(self):
        next_item = Node(10)
        node = Node(100)
        node.set_next(next_item)
        self.assertEqual(node.next, next_item)

    def test_next_None_set_manually(self):
        next_item = None
        node = Node(100)
        node.set_next(next_item)
        self.assertEqual(node.next, None)

    def test_next_NonNode_set_manually(self):
        next_item = list()
        node = Node(100)
        self.assertRaises(TypeError, lambda: node.set_next(next_item))


if __name__ == '__main__':
    unittest.main()
