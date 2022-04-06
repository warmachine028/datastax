import unittest
from typing import Optional, Any

from datastax.arrays import Queue
from datastax.errors import UnderFlowError, OverFlowError
from datastax.linkedlists import LinkedList


class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.limitedQueue = Queue(capacity=2)  # With fixed size Queue
        self.unlimitedQueue = Queue()  # With dynamic Queue

    def test_complete_fill_complete_empty(self):
        # Completely Filled
        self.limitedQueue.enqueue(10)
        self.limitedQueue.enqueue(20)

        # Should raise overflow error
        with self.assertRaises(OverFlowError):
            self.limitedQueue.enqueue(30)

        # Completely Emptied
        self.limitedQueue.dequeue()
        self.limitedQueue.dequeue()
        self.assertEqual([], self.items_in(self.limitedQueue))

    def test_construction(self):
        queue = Queue(capacity=5)  # With capacity more than Array size
        list(map(lambda item: queue.enqueue(item), [1, 2, 3]))
        self.assertEqual([1, 2, 3], self.items_in(queue))
        queue.enqueue(10)  # Then performing Enqueue Operation
        queue.enqueue(20)  # Again performing Enqueue Operation
        queue.dequeue()  # Performing Dequeue Operation
        self.assertEqual([2, 3, 10, 20], self.items_in(queue))
        queue = Queue()  # With first array element as None
        list(map(lambda item: queue.enqueue(item), [None, 1, 2]))
        self.assertEqual([None, 1, 2], self.items_in(queue))
        queue = Queue(capacity=None)  # With both arguments as None
        self.assertEqual([], self.items_in(queue))

    def test_dequeue_from_empty_queue(self):
        with self.assertRaises(UnderFlowError):
            self.limitedQueue.dequeue()
            self.unlimitedQueue.dequeue()

    def test_enqueue_in_empty_queue(self):
        self.limitedQueue.enqueue(50)
        self.assertEqual([50], self.items_in(self.limitedQueue))
        self.unlimitedQueue.enqueue(50)
        self.assertEqual([50], self.items_in(self.unlimitedQueue))

    def test_enqueue_in_full_queue(self):
        self.limitedQueue.enqueue(30)
        self.limitedQueue.enqueue(40)
        self.assertEqual([30, 40], self.items_in(self.limitedQueue))
        with self.assertRaises(OverFlowError):
            self.limitedQueue.enqueue(50)

        self.unlimitedQueue.enqueue(30)
        self.unlimitedQueue.enqueue(40)
        self.unlimitedQueue.enqueue(50)  # unlimited Queue, can't be full
        self.assertEqual([30, 40, 50], self.items_in(self.unlimitedQueue))

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
            Queue(capacity=3),  # -> self referential type
            None
        ]
        for item in items:
            self.unlimitedQueue.enqueue(item)

        self.assertEqual(items, self.items_in(self.unlimitedQueue))

    def test_string_repr(self):
        queue = Queue()
        operations = [
            ['enqueue', 30],
            ['enqueue', 20],
            ['enqueue', 40],
            'dequeue',
            'dequeue',
            ['enqueue', 50],
            'dequeue',
        ]
        results = [
            '\n'
            '         ┌──────┐\n'
            'FRONT -> │  30  │ <- REAR\n'
            '         └──────┘\n',

            '\n'
            '         ┌──────┬──────┐\n'
            'FRONT -> │  30  │  20  │ <- REAR\n'
            '         └──────┴──────┘\n',

            '\n'
            '         ┌──────┬──────┬──────┐\n'
            'FRONT -> │  30  │  20  │  40  │ <- REAR\n'
            '         └──────┴──────┴──────┘\n',

            '\n'
            '         ┌──────╥──────┬──────┐\n'
            'FRONT -> │  ╳   ║  20  │  40  │ <- REAR\n'
            '         └──────╨──────┴──────┘\n',

            '\n'
            '         ┌──────┬──────╥──────┐\n'
            'FRONT -> │  ╳   │  ╳   ║  40  │ <- REAR\n'
            '         └──────┴──────╨──────┘\n',

            '\n'
            '         ┌──────┬──────╥──────┬──────┐\n'
            'FRONT -> │  ╳   │  ╳   ║  40  │  50  │ <- REAR\n'
            '         └──────┴──────╨──────┴──────┘\n',

            '\n'
            '         ┌──────┬──────┬──────╥──────┐\n'
            'FRONT -> │  ╳   │  ╳   │  ╳   ║  50  │ <- REAR\n'
            '         └──────┴──────┴──────╨──────┘\n'

        ]
        operate = {
            'enqueue': lambda i: queue.enqueue(i),
            'dequeue': lambda _: queue.dequeue()
        }
        for item, result in zip(operations, results):
            operation, items = item if item[0] == 'enqueue' else (item, 0)
            operate[operation](items)
            self.assertEqual(result, queue.__str__())

    @staticmethod
    def items_in(queue: Queue) -> list[Optional[Any]]:
        return queue._array[queue.front:]


if __name__ == '__main__':
    unittest.main()
