from typing import Any, Optional, Self, Sequence
from datastax.Trees.BinaryTree import BinaryTree
from datastax.Nodes import TreeNode


class FibonacciTree(BinaryTree):
    _terms: Optional[int] = None
    _series: Optional[list] = None

    def __init__(self, terms: int):
        self._terms = terms
        self._series = None
        super().__init__([terms])

    @property
    def terms(self):
        return self._terms

    @property
    def series(self):
        self._series = []
        first, second = 0, 1
        if self._terms == 0:
            self._series.append(first)
        elif self._terms == 1:
            self._series.append(first)
            self._series.append(second)
        else:
            count = 0
            while count < self._terms + 1:
                self._series.append(first)
                first, second = second, first + second
                count += 1
        return self._series

    def _construct(self, items: Optional[Sequence] = None) -> Optional[Self]:
        print(not items, items)
        if not items or items[0] <= 0:
            return None
        n = items[0]
        self._root = self._fibonacci(n)
        return self

    def _fibonacci(self, n: int,
                   memo: Optional[dict[int, TreeNode]] = None) -> TreeNode:
        if memo is None:
            memo = {0: TreeNode(0), 1: TreeNode(1)}
        if n in memo:
            return memo[n]

        left, right = self._fibonacci(n - 1), self._fibonacci(n - 2, memo)
        memo[n] = TreeNode(left.data + right.data, left, right)
        return memo[n]

    def insert(self, item: Any):
        raise NotImplementedError

    def insert_path(self, data: Any, path: Optional[list[str]] = None) -> None:
        raise NotImplementedError
