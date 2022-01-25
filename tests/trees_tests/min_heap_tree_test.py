from __future__ import annotations

import random
import string
import unittest
from typing import Any

from datastax.errors import DeletionFromEmptyTree
from datastax.trees import MinHeapTree, HeapTreeNode
from tests.trees_tests.common_helper_functions import level_wise_items


class TestMinHeapTree(unittest.TestCase):

    def setUp(self) -> None:
        self.mht = MinHeapTree()
        self.test_cases = 10
        self.max_sample_size = 10
        self.print_test_cases = [
            [1],
            [None, 10],
            [10, None, None],
            ['root', None, None, 'child'],
            ["1", "B", "Baxy", "D"],
            [1, None, 2, 3, None, None, 4, 5]
        ]

    def test_array_representation(self):
        testcases = [
            [*range(10)],
            [None, 10],
            [10, None, None],
            ['root', None, None, 'child']
        ]

        for testcase in testcases:
            tree = MinHeapTree(testcase)
            self.assertEqual(self.min_heapify(testcase), tree.array_repr)

    def test_construction(self):
        items = [
            [1, 2, 3, 4, 5, 6],  # <- Using general list of ints
            [*range(10)],  # <- Using range object unpacking in list
            [],  # <- Using Empty list
            [None],  # <- Using only None item passed through list
            [None, 1, 2, 3, 4, 5],  # <- Using First item as None
            None,  # <- Using None passed directly
        ]

        for item in items:
            result: list[list[Any]] = [self.min_heapify(item)]
            tree = MinHeapTree(item)
            result.append(result[0][0] if result[0] else None)
            # checking tree items
            self.assertEqual(result[0], level_wise_items(tree))
            # checking root
            self.assertEqual(result[1], tree.root.data if tree.root else None)

        # Construct with existing root
        root_node = HeapTreeNode(10)
        tree = MinHeapTree([*range(9, 0, -1)], root=root_node)
        self.assertEqual(self.min_heapify([10, *range(9, 0, -1)]),
                         level_wise_items(tree))

    def test_heappush(self):
        # inserting using insert_path
        with self.assertRaises(NotImplementedError):
            self.mht.insert(10)
        self.assertEqual([], level_wise_items(self.mht))

        # testing heappush
        data = [4, 3, 1, 2, 5, 3, 2, 1, 9]

        for i, item in enumerate(data, 1):
            self.mht.heappush(item)
            self.assertEqual(self.min_heapify(data[:i]),
                             level_wise_items(self.mht))

    def test_heappop(self):
        for i in range(self.test_cases):
            test_case = []
            for _ in range(self.max_sample_size):
                test_case.append(random.choice(range(-100, 100)))
            tree = MinHeapTree(test_case)
            result = [tree.heappop() for _ in tree.array_repr]
            self.assertEqual(sorted(test_case), result)

            # Must warn when tree is Empty
            with self.assertWarns(DeletionFromEmptyTree):
                self.assertEqual(None, tree.heappop())

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
            MinHeapTree([1, 2]).root,  # -> Node
            MinHeapTree([1, 2]),  # ->  self referential type
            None  # -> * can't be inserted anywhere
            # entire list will be discarded if Node as first element
        ]  # Can't even insert the rest of the items

        # Can't perform comparison operation between heterogeneous items
        with self.assertRaises(TypeError):
            MinHeapTree(items)

    def test_preorder_print(self):

        results = [
            '\n1', 'NULL', '\n10', '\nchild'
                                   '\n└─▶ root',

            '\n1'
            '\n├─▶ B'  # Normal MinHeapTree Repr
            '\n│   └─▶ D'
            '\n└─▶ Baxy',

            '\n1'
            '\n├─▶ 2'
            '\n│   ├─▶ 4'  # An example of a complete binary tree
            '\n│   └─▶ 5'
            '\n└─▶ 3',

        ]

        for testcase, result in zip(self.print_test_cases, results):
            tree = MinHeapTree(testcase)
            self.assertEqual(result, tree.preorder_print())

    def test_string_representation(self):
        results = [
            '   1  \n', '  NULL', '  10  \n',
            '        child       \n'
            '     ┌────┘         \n'
            '   root             \n',

            '                1               \n'
            '        ┌───────┴───────┐       \n'
            '        B             Baxy      \n'  # Normal MinHeapTree Repr
            '    ┌───┘                       \n'
            '    D                           \n',
            '            1           \n'
            '      ┌─────┴─────┐     \n'
            '      2           3     \n'  # An example of a complete binary
            '   ┌──┴──┐              \n'  # Tree
            '   4     5              \n'
        ]

        for testcase, result in zip(self.print_test_cases, results):
            tree = MinHeapTree(testcase)
            self.assertEqual(result, tree.__str__())

    def test_with_random_inputs(self):
        numbers = range(-100, 100)
        characters = string.ascii_uppercase + string.ascii_lowercase
        # To avoid terminal explosion please avoid printing these trees
        # after construction
        for _ in range(self.test_cases):
            sample_size = random.randint(1, self.max_sample_size)
            sample = random.sample(numbers, sample_size)

            # Constructing tree with random numbers
            tree = MinHeapTree(sample)
            self.assertEqual(self.min_heapify(sample),
                             level_wise_items(tree))

            sample_size = random.randint(1, len(characters))
            sample = random.sample(characters, sample_size)

            # Constructing tree with random character set
            tree = MinHeapTree(sample)
            self.assertEqual(self.min_heapify(sample),
                             level_wise_items(tree))

        # Try insertion with duplicates
        sample_size = random.randint(1, self.max_sample_size)
        random_sample = random.sample(numbers, sample_size)
        for _ in range(1, random.randint(2, 10)):
            random_sample.append(random.choice(random_sample))

        tree = MinHeapTree(random_sample)
        self.assertEqual(self.min_heapify(random_sample),
                         level_wise_items(tree))

    @staticmethod
    def min_heapify(test_case: list[Any]) -> list[Any]:
        heap: list[Any] = []

        def heapify(index):
            root = index
            left_child, right_child = root * 2 + 1, root * 2 + 2
            if left_child < n and heap[left_child] < heap[root]:
                root = left_child
            if right_child < n and heap[right_child] < heap[root]:
                root = right_child
            if root != index:
                heap[index], heap[root] = heap[root], heap[index]
                heapify(root)

        if not test_case or test_case[0] is None:
            return heap
        for i, item in enumerate(filter(lambda x: x is not None, test_case)):
            heap.append(item)
            n = len(heap)
            for j in range(n // 2 - 1, -1, -1):
                heapify(j)

        return heap


if __name__ == '__main__':
    unittest.main()
