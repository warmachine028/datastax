import random
import unittest
from datastax.Trees import SumSegmentTree


class TestSumSegmentTree(unittest.TestCase):
    def setUp(self) -> None:
        self.seg_tree = SumSegmentTree()
        self.test_cases = 10
        self.max_sample_size = 10

    def test_construction(self):
        input_list = [2, 3, 1, 4, 2, 5, 2, 3, 1, 5]
        tree = SumSegmentTree(input_list)

        result = (
            '                                               '
            '28                                               \n'
            '                                              '
            '[0:9]                                             \n'
            '                        '
            '┌───────────────────────┴───────────────────────┐ '
            '                      \n'
            '                       12                          '
            '                    '
            '16                       \n'
            '                      [0:4]                        '
            '                   '
            '[5:9]                     \n'
            '            ┌───────────┴───────────┐              '
            '         '
            '┌───────────┴───────────┐           \n'
            '            6                       6              '
            '        '
            '10                       6           \n'
            '          [0:2]                   [3:4]            '
            '       '
            '[5:7]                   [8:9]         \n'
            '      ┌─────┴─────┐           ┌─────┴─────┐        '
            '   '
            '┌─────┴─────┐           ┌─────┴─────┐     \n'
            '      5           1           4           2        '
            '   7           '
            '3           1           5     \n'
            '    [0:1]                                           '
            '[5:6]                                       \n'
            '   ┌──┴──┐                                         '
            '┌──┴──┐                                      \n'
            '   2     3                                         '
            '5     '
            '2                                      \n'
            '                                                   '
            '                                             \n'
        )

        self.assertEqual(str(tree), result)

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
        input_list = [2, 3, 1, 4, 2, 5, 2, 3, 1, 5]
        tree = SumSegmentTree(input_list)

        # Update the range [3, 9] with +5
        tree.update_at_range(3, 9, +5)
        result = (
            '                                               '
            '63                                               \n'
            '                                              '
            '[0:9]                                             \n'
            '                        '
            '┌───────────────────────┴───────────────────────┐                       \n'
            '                       22                                              '
            '41                       \n'
            '                      [0:4]                                           '
            '[5:9]                     \n'
            '            ┌───────────┴───────────┐                       '
            '┌───────────┴───────────┐           \n'
            '            6                      16                      '
            '10                       6           \n'
            '          [0:2]                   [3:4]                   '
            '[5:7]                   [8:9]         \n'
            '      ┌─────┴─────┐           ┌─────┴─────┐           '
            '┌─────┴─────┐           ┌─────┴─────┐     \n'
            '      5           1           4           2           7           '
            '3           1           5     \n'
            '    [0:1]                                           '
            '[5:6]                                       \n'
            '   ┌──┴──┐                                         '
            '┌──┴──┐                                      \n'
            '   2     3                                         5     '
            '2                                      \n'
            '                                                                                                \n'
        )

        self.assertEqual(str(tree), result)

        # Update the range [5, 8] with +3
        tree.update_at_range(5, 8, +3)
        result = (
            '                                                               '
            '255                                                              \n'
            '                                                              '
            '[0:9]                                                             \n'
            '                                '
            '┌───────────────────────────────┴───────────────────────────────┐                               \n'
            '                               '
            '22                                                              '
            '233                              \n'
            '                              '
            '[0:4]                                                           '
            '[5:9]                             \n'
            '                '
            '┌───────────────┴───────────────┐                               '
            '┌───────────────┴───────────────┐               \n'
            '                6                              '
            '16                              142                             '
            '91               \n'
            '              [0:2]                           '
            '[3:4]                           [5:7]                           '
            '[8:9]             \n'
            '        ┌───────┴───────┐               ┌───────┴───────┐               '
            '┌───────┴───────┐               ┌───────┴───────┐       \n'
            '        5               1               4               2               '
            '7               3              45              46       \n'
            '      [0:1]                                                           '
            '[5:6]                                                     \n'
            '    ┌───┴───┐                                                       '
            '┌───┴───┐                                                   \n'
            '    2       3                                                       5       '
            '2                                                   \n'
            '                                                               '
            '                                                                 \n'
        )

        self.assertEqual(str(tree), result)

        # Get the sum of the range [3, 5]
        self.assertEqual(tree.get_sum(3, 5), 204)

        # Check segment array after the first update
        expected_segment_array = [2, 3, 1, 4, 2, 188, 185, 186, 45, 46]
        self.assertEqual(tree.segment_array, expected_segment_array)

        # Check segment array second time
        self.assertEqual(tree.segment_array, expected_segment_array)


if __name__ == '__main__':
    unittest.main()
