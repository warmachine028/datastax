from __future__ import annotations

import unittest

from datastax.trees import SumSegmentTree


class TestSumSegmentTree(unittest.TestCase):
    def setUp(self) -> None:
        self.m_seg_tree = SumSegmentTree()

    def test(self):
        tree = SumSegmentTree([1, 2, 3, 4, 5])
        print(tree)
        tree.update_at_index(2, 5)
        print(tree)
        print(tree.get_sum(1, 3))

    def test_2(self):
        tree = SumSegmentTree([1, 3, 5, 7, 9, 11])
        print(tree)
        print(tree.preorder_print())

    def test_3(self):
        tree = SumSegmentTree([[i] for i in range(5)])

        print(tree)
        print(tree.root)
        print(tree.get_sum(1, 4))
        tree.update_at_index(3, [997])
        tree.update_at_index(0, [99])
        tree.update_at_index(4, [89])
        print(tree)

    def test_4(self):
        tree = SumSegmentTree()
        print(tree)

        tree = SumSegmentTree("Hello World")
        print(tree.get_sum(1, 4))
        tree.update_at_index(3, "z")


if __name__ == '__main__':
    unittest.main()
