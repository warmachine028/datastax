from __future__ import annotations

import random
import unittest
# from itertools import chain

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

    # def test_get_sum_with_lists(self):
    #     for _ in range(self.test_cases):
    #         min_, max_ = 1, 101
    #         sample = random.sample(range(min_, max_), self.max_sample_size)
    #         sample = [[item] for item in sample]
    #         tree = SumSegmentTree(sample)
    #         for _ in range(self.test_cases * 10):
    #             left = random.randint(min_, max_)
    #             right = random.randint(left, max_)
    #             self.assertEqual(list(chain(*sample[left:right + 1])),
    #                              tree.get_sum(left, right))

    # def test_get_sum_with_strings(self):
    #     for _ in range(self.test_cases):
    #         min_, max_ = 1, 101
    #         sample = random.sample(range(min_, max_), self.max_sample_size)
    #         sample = ''.join(chr(item) for item in sample)
    #         tree = SumSegmentTree(sample)
    #         for _ in range(self.test_cases * 10):
    #             left = random.randint(min_, max_)
    #             right = random.randint(left, max_)
    #             self.assertEqual(''.join(sample[left:right + 1]),
    #                              tree.get_sum(left, right))

    def test_3(self):
        tree = SumSegmentTree([2, 3, 1, 4, 2, 5, 2, 3, 1, 5])
        # tree = SumSegmentTree()
        print(tree)
        tree.update_at_range(3, 9, +5)
        print(tree)
        tree.update_at_range(5, 8, +3)
        print(tree.get_sum(3, 5))
        print(tree)
        print(tree.lazy_tree)
        print(tree.segment_array)
        # print(tree)
        # print(tree.lazy_tree)


if __name__ == '__main__':
    unittest.main()
