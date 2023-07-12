import sys
import unittest
from typing import Optional, Any
from datastax.errors import UnderFlowError, OverFlowError
from datastax.Lists import Queue, LinkedList


class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.limitedQueue = Queue(2)  # With fixed size Queue
        self.unlimitedQueue = Queue()  # With dynamic Queue

    def test_append_and_insert(self):
        item = 10
        self.assertRaises(
            NotImplementedError, lambda: self.limitedQueue.append(item))
        self.assertRaises(
            NotImplementedError, lambda: self.limitedQueue.insert(item))

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
        queue = Queue(None, [1, 2, 3, 4, 5])  # With Array Without capacity
        self.assertEqual([1, 2, 3, 4, 5], self.items_in(queue))
        queue = Queue(5, [1, 2, 3, 4, 5])  # With Array With capacity
        self.assertEqual([1, 2, 3, 4, 5], self.items_in(queue))
        queue = Queue(5)  # Without Array With capacity
        self.assertEqual([], self.items_in(queue))
        queue = Queue()  # Without Array Without capacity
        self.assertEqual([], self.items_in(queue))
        queue = Queue(3, [1, 2, 3, 4])  # With capacity less than Array size
        self.assertEqual([1, 2, 3], self.items_in(queue))
        queue = Queue(5, [1, 2, 3])  # With capacity more than Array size
        self.assertEqual([1, 2, 3], self.items_in(queue))
        queue.enqueue(10)  # Then performing Enqueue Operation
        queue.enqueue(20)  # Again performing Enqueue Operation
        queue.dequeue()  # Performing Dequeue Operation
        self.assertEqual([2, 3, 10, 20], self.items_in(queue))
        queue = Queue(None, [None, 1, 2])  # With first array element as None
        self.assertEqual([None, 1, 2], self.items_in(queue))
        queue = Queue(None, None)  # With both arguments as None
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

    def test_queue_insertion_deletion(self):
        queue = self.unlimitedQueue
        self.assertEqual([], self.items_in(self.unlimitedQueue))
        queue.enqueue(10)
        self.assertEqual([10], self.items_in(self.unlimitedQueue))
        queue.dequeue()
        self.assertEqual([], self.items_in(self.unlimitedQueue))
        queue.enqueue(20)
        self.assertEqual([20], self.items_in(self.unlimitedQueue))

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
            Queue(3, [1, 2, 3]),  # -> self referential type
            None  # -> * can't be inserted as first item but otherwise okay...
            # entire list will be discarded if Node as first element
        ]
        for item in items:
            self.unlimitedQueue.enqueue(item)

        self.assertEqual(items, self.items_in(self.unlimitedQueue))

    def test_set_capacity(self):
        # Test case: Capacity 10
        # Test case: Valid capacity
        try:
            queue = Queue(10)
            self.assertEqual(queue.capacity, 10)
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")
        # Test case: Capacity 0
        # Test case: Useless capacity
        try:
            queue = Queue(0)
            self.assertEqual(queue.capacity, 0)
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")
        # Test case: Negative capacity
        with self.assertRaises(ValueError):
            Queue(-1)

        # Test case: Float capacity
        with self.assertRaises(TypeError):
            Queue(4.5)

        # Test case: None capacity
        try:
            queue = Queue(None)
            self.assertEqual(queue.capacity, sys.maxsize)
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")

        # Test case: No capacity argument
        try:
            queue = Queue(None)
            self.assertEqual(queue.capacity, sys.maxsize)
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")

    @staticmethod
    def items_in(queue: Queue) -> list[Optional[Any]]:
        result = []
        head = queue.head
        while head:
            result.append(head.data)
            head = head.next
        return result


if __name__ == '__main__':
    unittest.main()
