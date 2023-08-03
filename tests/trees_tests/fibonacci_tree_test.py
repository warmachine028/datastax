import unittest
from datastax.Trees import FibonacciTree
from datastax.Nodes import TreeNode


class TestFibonacciTree(unittest.TestCase):
    def setUp(self) -> None:
        self.fibTree = FibonacciTree(1)

    @staticmethod
    def get_fibonacci_series(n, memo=None):
        if memo is None:
            memo = {0: 0, 1: 1}

        if n in memo:
            return [memo[i] for i in range(n + 1)]

        series = TestFibonacciTree.get_fibonacci_series(n - 1, memo)
        memo[n] = memo[n - 1] + memo[n - 2]
        series.append(memo[n])
        return series

    def test_series_property(self):
        for i in range(10):
            self.fibTree = FibonacciTree(i)
            self.assertEqual(self.fibTree.series, TestFibonacciTree.get_fibonacci_series(i))

    def test_construct_with_valid_n(self):
        for i in range(10):
            tree = FibonacciTree(i)
            if i == 0:
                self.assertIsNone(tree.root)
                continue
            self.assertIsNotNone(tree.root)
            self.assertIsInstance(tree.root, TreeNode)
            self.assertEqual(tree.root.data, TestFibonacciTree.get_fibonacci_series(i)[-1])

    def test_construct_with_invalid_n(self):
        tree = FibonacciTree(-1)
        self.assertIsNone(tree.root)


if __name__ == '__main__':
    unittest.main()
