from __future__ import annotations

import random
import unittest
from itertools import chain

from datastax.trees import SumSegmentTree


class TestSumSegmentTree(unittest.TestCase):
    def setUp(self) -> None:
        self.seg_tree = SumSegmentTree()
        self.test_cases = 10
        self.max_sample_size = 10

    def test_get_sum_queries(self):
        for _ in range(self.test_cases):
            min_, max_ = 1, 101
            sample = random.sample(range(min_, max_), self.max_sample_size)
            tree = SumSegmentTree(sample)
            for _ in range(self.test_cases):
                left = random.randint(min_, max_)
                right = random.randint(left, max_)
                self.assertEqual(sum(sample[left:right + 1]),
                                 tree.get_sum(left, right))

    def test_get_sum_with_lists(self):
        for _ in range(self.test_cases):
            min_, max_ = 1, 101
            sample = random.sample(range(min_, max_), self.max_sample_size)
            sample = [[item] for item in sample]
            tree = SumSegmentTree(sample)
            for _ in range(self.test_cases * 10):
                left = random.randint(min_, max_)
                right = random.randint(left, max_)
                self.assertEqual(list(chain(*sample[left:right + 1])),
                                 tree.get_sum(left, right))

    def test_get_sum_with_strings(self):
        for _ in range(self.test_cases):
            min_, max_ = 1, 101
            sample = random.sample(range(min_, max_), self.max_sample_size)
            sample = ''.join(chr(item) for item in sample)
            tree = SumSegmentTree(sample)
            for _ in range(self.test_cases * 10):
                left = random.randint(min_, max_)
                right = random.randint(left, max_)
                self.assertEqual(''.join(sample[left:right + 1]),
                                 tree.get_sum(left, right))

    def test_3(self):
        tree = SumSegmentTree([[i] for i in range(5)])

        print(tree)
        print(tree.root)
        print(tree.get_sum(1, 4))
        tree.update_at_index(3, [997])
        tree.update_at_index(0, [99])
        tree.update_at_index(4, [89])
        print(tree)


if __name__ == '__main__':
    unittest.main()
