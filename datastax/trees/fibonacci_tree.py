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

        self._root = self._fibonacci(n)
        return self

    def _fibonacci(self, n: int,
                   memo: dict[int, TreeNode] = None) -> TreeNode:
        if memo is None:
            memo = {0: TreeNode(0), 1: TreeNode(1)}
        if n in memo:
            return memo[n]

        left, right = self._fibonacci(n - 1), self._fibonacci(n - 2, memo)
        memo[n] = TreeNode(left.data + right.data, left, right)
        return memo[n]

    def insert(self, item: Any):
        raise NotImplementedError
