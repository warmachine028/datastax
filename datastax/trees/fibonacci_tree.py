# Fibonacci Tree Implementation
from __future__ import annotations

from typing import Optional, Any

from datastax.trees.private_trees.binary_tree import BinaryTree, TreeNode


class FibonacciTree(BinaryTree):
    def __init__(self, nth: int = None):
        self._n = nth
        self._series = None
        super().__init__(nth)

    @property
    def series(self):
        self._series = []
        first, second = 0, 1
        if self._n == 0:
            self._series.append(first)
        elif self._n == 1:
            self._series.append(first)
            self._series.append(second)
        else:
            count = 0
            while count < self._n + 1:
                self._series.append(first)
                first, second = second, first + second
                count += 1
        return self._series

    def _construct(self, n: int = None) -> Optional[FibonacciTree]:
        if n is None or n < 0:
            return None

        self._root = self.fibonacci(n)
        return self

    def fibonacci(self, n: int):
        if n == 0:
            return TreeNode(0)
        if n == 1:
            return TreeNode(1)
        else:
            left = self.fibonacci(n - 1)
            right = self.fibonacci(n - 2)
            return TreeNode(left.data + right.data, left, right)

    def insert(self, item: Any):
        raise NotImplementedError
