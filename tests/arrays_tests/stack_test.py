import unittest
from typing import Optional, Any

from datastax.Arrays import Stack
from datastax.Utils.Exceptions import UnderflowException, OverflowException
from datastax.Lists import LinkedList


class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.limitedStack = Stack(capacity=2)  # With fixed size Stack
        self.unlimitedStack = Stack()  # With dynamic Stack

    def test_complete_fill_complete_empty(self):
        # Completely Filled
        self.limitedStack.push(10)
        self.limitedStack.push(20)

        # Should raise overflow error
        with self.assertRaises(OverflowException):
            self.limitedStack.push(30)

        # Completely Emptied
        self.limitedStack.pop()
        self.limitedStack.pop()
        self.assertEqual([], self.items_in(self.limitedStack))

    def test_construction(self):
        stack = Stack(capacity=5)  # With capacity more than Array size
        list(map(lambda item: stack.push(item), [1, 2, 3]))
        self.assertEqual([1, 2, 3], self.items_in(stack))
        stack.push(10)  # Then performing Enqueue Operation
        stack.push(20)  # Again performing Enqueue Operation
        stack.pop()  # Performing Dequeue Operation
        self.assertEqual([1, 2, 3, 10], self.items_in(stack))
        stack = Stack()  # With first array element as None
        list(map(lambda item: stack.push(item), [None, 1, 2]))
        self.assertEqual([None, 1, 2], self.items_in(stack))
        stack = Stack(capacity=None)  # With both arguments as None
        self.assertEqual([], self.items_in(stack))

    def test_dequeue_from_empty_queue(self):
        with self.assertRaises(UnderflowException):
            self.limitedStack.pop()
            self.unlimitedStack.pop()

    def test_enqueue_in_empty_queue(self):
        self.limitedStack.push(50)
        self.assertEqual([50], self.items_in(self.limitedStack))
        self.unlimitedStack.push(50)
        self.assertEqual([50], self.items_in(self.unlimitedStack))

    def test_enqueue_in_full_queue(self):
        self.limitedStack.push(30)
        self.limitedStack.push(40)
        self.assertEqual([30, 40], self.items_in(self.limitedStack))
        with self.assertRaises(OverflowException):
            self.limitedStack.push(50)

        self.unlimitedStack.push(30)
        self.unlimitedStack.push(40)
        self.unlimitedStack.push(50)  # unlimited Stack, can't be full
        self.assertEqual([30, 40, 50], self.items_in(self.unlimitedStack))

    def test_enqueueing_heterogeneous_items(self):
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
            LinkedList([1, 2]),  # ->  LinkedList
            Stack(capacity=3),  # -> self referential type
            None
        ]
        for item in items:
            self.unlimitedStack.push(item)

        self.assertEqual(items, self.items_in(self.unlimitedStack))

    def test_string_repr(self):
        stack = Stack(capacity=3)
        operations = [
            'display',
            ['push', 30],
            ['push', 20],
            ['push', 40],
            'pop',
            'pop',
            ['push', 50],
            'pop',
        ]
        results = [
            '│STACK EMPTY│\n'
            '╰───────────╯\n',

            '│           │\n'
            ':           :\n'
            '├───────────┤\n'
            '│     30    │ <- TOP\n'
            '╰───────────╯\n',

            '│           │\n'
            ':           :\n'
            '├───────────┤\n'
            '│     20    │ <- TOP\n'
            '├───────────┤\n'
            '│     30    │\n'
            '╰───────────╯\n',

            '┌───────────┐\n'
            '│     40    │ <- TOP\n'
            '├───────────┤\n'
            '│     20    │\n'
            '├───────────┤\n'
            '│     30    │\n'
            '╰───────────╯\n',

            '│           │\n'
            ':           :\n'
            '├───────────┤\n'
            '│     20    │ <- TOP\n'
            '├───────────┤\n'
            '│     30    │\n'
            '╰───────────╯\n',

            '│           │\n'
            ':           :\n'
            '├───────────┤\n'
            '│     30    │ <- TOP\n'
            '╰───────────╯\n',

            '│           │\n'
            ':           :\n'
            '├───────────┤\n'
            '│     50    │ <- TOP\n'
            '├───────────┤\n'
            '│     30    │\n'
            '╰───────────╯\n',

            '│           │\n'
            ':           :\n'
            '├───────────┤\n'
            '│     30    │ <- TOP\n'
            '╰───────────╯\n',
        ]
        operate = {
            'push': lambda i: stack.push(i),
            'pop': lambda _: stack.pop(),
            'display': lambda _: None
        }
        for item, result in zip(operations, results):
            operation, items = item if item[0] == 'push' else (item, 0)
            operate[operation](items)
            self.assertEqual(result, stack.__str__())

    def test_peek_with_limited_stack(self):
        self.perform_operations(self.limitedStack)

    def test_peek_with_unlimited_stack(self):
        self.perform_operations(self.unlimitedStack)

    def perform_operations(self, stack: Stack):
        stack.push(10)
        self.assertEqual(10, stack.peek())
        stack.push(20)
        self.assertEqual(20, stack.peek())
        self.assertEqual(20, stack.pop())
        self.assertEqual(10, stack.peek())
        self.assertEqual(10, stack.pop())
        self.assertEqual("STACK EMPTY", stack.peek())

    @staticmethod
    def items_in(stack: Stack) -> list[Optional[Any]]:
        return stack.array


if __name__ == '__main__':
    unittest.main()
