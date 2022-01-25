from __future__ import annotations

import unittest

from datastax.trees import MinSegmentTree


class TestMinSegmentTree(unittest.TestCase):
    def setUp(self) -> None:
        self.m_seg_tree = MinSegmentTree()

    def test(self):
        tree = MinSegmentTree([1, 2, 3, 4, 5])
        print(tree)
        tree.update_at_index(2, 99)
        print(tree)
        print(tree.get_min(2, 4))
        print(tree.preorder_print())
        tree = MinSegmentTree([1, 3, 5, 7, 9, 11])
        print(tree)
        print(tree.preorder_print())

        tree = MinSegmentTree([[i] for i in range(10)])
        print(tree)
        tree.update_at_index(3, [-99])
        print(tree)
        print(tree.root)
        print(tree.get_min(3, 7))
        tree = MinSegmentTree()
        print(tree)
        tree = MinSegmentTree("MinSegmentTree")
        print(tree)
        print(tree.get_min(2, 3))


if __name__ == '__main__':
    unittest.main()
