import random
import unittest
from typing import Optional, Any

from datastax.Arrays import PriorityQueue
from datastax.errors import UnderFlowError, OverFlowError


class TestPriorityQueue(unittest.TestCase):

    def setUp(self) -> None:
        # With fixed size PriorityQueue
        self.limitedPriorityQueue = PriorityQueue(capacity=2)
        # With dynamic PriorityQueue
        self.unlimitedPriorityQueue = PriorityQueue()

    def test_complete_fill_complete_empty(self):
        # Completely Filled
        self.limitedPriorityQueue.enqueue(10)
        self.limitedPriorityQueue.enqueue(20)

        # Should raise overflow error
        with self.assertRaises(OverFlowError):
            self.limitedPriorityQueue.enqueue(30)

        # Completely Emptied
        self.limitedPriorityQueue.dequeue()
        self.limitedPriorityQueue.dequeue()
        self.assertEqual([], self.items_in(self.limitedPriorityQueue))

    def test_construction(self):
        queue = PriorityQueue(capacity=5)  # With capacity more than Array size
        list(map(lambda item: queue.enqueue(item), [1, 2, 3]))
        self.assertEqual([3, 1, 2], self.items_in(queue))
        queue.enqueue(10)  # Then performing Enqueue Operation
        queue.enqueue(20)  # Again performing Enqueue Operation
        queue.dequeue()  # Performing Dequeue Operation
        self.assertEqual([10, 3, 2, 1], self.items_in(queue))
        queue = PriorityQueue()  # With first array element as None
        with self.assertRaises(TypeError):
            list(map(lambda item: queue.enqueue(item), [None, 1, 2]))
        queue = PriorityQueue(capacity=None)  # With both arguments as None
        self.assertEqual([], self.items_in(queue))

    def test_dequeue_from_empty_queue(self):
        with self.assertRaises(UnderFlowError):
            self.limitedPriorityQueue.dequeue()
            self.unlimitedPriorityQueue.dequeue()

    def test_enqueue_in_empty_queue(self):
        self.limitedPriorityQueue.enqueue(50)
        self.assertEqual([50], self.items_in(self.limitedPriorityQueue))
        self.unlimitedPriorityQueue.enqueue(50)
        self.assertEqual([50], self.items_in(self.unlimitedPriorityQueue))

    def test_enqueue_in_full_queue(self):
        self.limitedPriorityQueue.enqueue(30)
        self.limitedPriorityQueue.enqueue(40)
        self.assertEqual([40, 30], self.items_in(self.limitedPriorityQueue))
        with self.assertRaises(OverFlowError):
            self.limitedPriorityQueue.enqueue(50)

        self.unlimitedPriorityQueue.enqueue(30)
        self.unlimitedPriorityQueue.enqueue(40)
        # unlimited PriorityQueue, can't be full
        self.unlimitedPriorityQueue.enqueue(50)
        self.assertEqual([50, 30, 40],
                         self.items_in(self.unlimitedPriorityQueue))

    def test_sorting(self):
        _range = random.randrange(1, 100)
        sample = random.sample(range(100), _range)
        n = len(sample)

        # Priority Queue
        p_queue = PriorityQueue(capacity=n)
        for item in sample:
            p_queue.enqueue(item)
        self.assertEqual(sorted(sample),
                         [p_queue.dequeue() for _ in range(n)][::-1])

    def test_string_repr(self):
        queue = PriorityQueue()
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
            'FRONT -> │  40  │  20  │  30  │ <- REAR\n'
            '         └──────┴──────┴──────┘\n',

            '\n'
            '         ┌──────┬──────┐\n'
            'FRONT -> │  30  │  20  │ <- REAR\n'
            '         └──────┴──────┘\n',

            '\n'
            '         ┌──────┐\n'
            'FRONT -> │  20  │ <- REAR\n'
            '         └──────┘\n',

            '\n'
            '         ┌──────┬──────┐\n'
            'FRONT -> │  50  │  20  │ <- REAR\n'
            '         └──────┴──────┘\n',

            '\n'
            '         ┌──────┐\n'
            'FRONT -> │  20  │ <- REAR\n'
            '         └──────┘\n',
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
    def items_in(queue: PriorityQueue) -> list[Optional[Any]]:
        return queue._array[queue.front:]


if __name__ == '__main__':
    unittest.main()
