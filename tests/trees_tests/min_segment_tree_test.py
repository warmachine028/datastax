from __future__ import annotations

import unittest

from datastax.trees import MinSegmentTree


class TestMinSegmentTree(unittest.TestCase):
    def setUp(self) -> None:
        self.m_seg_tree = MinSegmentTree()

    def test(self):
        tree = MinSegmentTree([2, 3, 1, 4, 2, 5, 2, 3, 1, 5])
        # tree = MinSegmentTree()
        print(tree)
        tree.update_at_range(3, 9, -5)
        print(tree)
        tree.update_at_range(5, 8, +3)
        print(tree.get_min(3, 5))
        print(tree)
        print(tree.lazy_tree)
        print(tree.segment_array)
        print(tree)
        print(tree.lazy_tree)


if __name__ == '__main__':
    unittest.main()
