import unittest
from datastax.Trees import MinSegmentTree


class TestMinSegmentTree(unittest.TestCase):
    def setUp(self) -> None:
        self.m_seg_tree = MinSegmentTree()

    def test(self):
        tree = MinSegmentTree([2, 3, 1, 4, 2, 5, 2, 3, 1, 5])
        # tree = MinSegmentTree()
        print(tree.segment_array)  # [2, 3, 1, 4, 2, 5, 2, 3, 1, 5]
        tree.update_at_range(3, 9, -5)
        print(tree.segment_array)  # [2, 3, 1, 4, 2, 5, 2, 3, 1, 5]
        tree.update_at_range(5, 8, +3)
        print(tree.get_min(3, 5))  # -5
        print(tree.segment_array)  # [2, 3, 1, 4, 2, -5, -5, -5, -5, -5]
        print(
            tree.lazy_tree.segment_array)  # [9223372036854775807, 9223372036854775807, 9223372036854775807, -5, -5, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
        print(tree.segment_array)  # [2, 3, 1, 4, 2, -5, -5, -5, -5, -5]


if __name__ == '__main__':
    unittest.main()
