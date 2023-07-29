import unittest

from datastax.Trees import FibonacciTree


class TestFibonacciTree(unittest.TestCase):
    def setUp(self) -> None:
        self.hufT = FibonacciTree()

    def test(self):
        for i in range(10):
            tree = FibonacciTree(i)
            print(tree)
            print(tree.series)


if __name__ == '__main__':
    unittest.main()
