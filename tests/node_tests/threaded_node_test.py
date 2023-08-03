import unittest
from datastax.Nodes import ThreadedNode


class TestThreadedNode(unittest.TestCase):

    def _test_string(self):
        result = \
            '         \n' \
            '│   1   │\n' \
            '└───┴───┘\n'
        self.assertEqual(str(ThreadedNode(1)), result)
        result = \
            '         \n' \
            '│   12  │\n' \
            '└───┴───┘\n'
        self.assertEqual(str(ThreadedNode(12)), result)
        result = \
            '           \n' \
            '│   123   │\n' \
            '└────┴────┘\n'
        self.assertEqual(str(ThreadedNode(123)), result)

    def _test_string_with_left(self):
        result = \
            ('  \n'
             '    1     │\n'
             '┌───┴───┘\n'
             '20')
        self.assertEqual(str(ThreadedNode(1, ThreadedNode(20))), result)
        # result = \
        #     '         \n' \
        #     '│   12  │\n' \
        #     '└───┴───┘\n'
        # self.assertEqual(str(ThreadedNode(12)), result)
        # result = \
        #     '           \n' \
        #     '│   123   │\n' \
        #     '└────┴────┘\n'
        # self.assertEqual(str(ThreadedNode(123)), result)


if __name__ == '__main__':
    unittest.main()
