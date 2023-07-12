# Priority Queue implementation using Lists (Pseudo Arrays)
from typing import Any, Callable, Optional

from datastax.Arrays.Queue import Queue
from datastax.errors import OverFlowError, UnderFlowError


class PriorityQueue(Queue):
    comparator: Callable

    def __init__(self, *, capacity: Optional[int] = None,
                 custom_comparator: Optional[Callable] = None):
        super().__init__(capacity=capacity)
        self.comparator = custom_comparator or max

    def swap(self, index1: int, index2: int) -> None:
        array = self._array
        array[index1], array[index2] = array[index2], array[index1]

    def heapify(self, index: int, length: int) -> None:
        root = index
        left_child = root * 2 + 1
        right_child = root * 2 + 2
        if left_child < length and (
                self.comparator(self.array[left_child],
                                self.array[root]) == self.array[left_child]
        ):
            root = left_child
        if right_child < length and (
                self.comparator(self.array[right_child],
                                self.array[root]) == self.array[right_child]
        ):
            root = right_child
        if root == index:
            return
        self.swap(root, index)
        self.heapify(root, length)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise UnderFlowError(self)

        deleted_item = self._array[self._front]
        self._array[self._front] = self._array[-1]
        self._array.pop()
        self._rear -= 1
        self.heapify(0, len(self.array))
        return deleted_item

    def enqueue(self, item: Any) -> int:
        if self.is_full():
            raise OverFlowError(self)

        self._array.append(item)
        self._rear += 1
        n = len(self.array)
        for i in range(n // 2 - 1, -1, -1):
            try:
                self.heapify(i, n)
            except TypeError:
                raise TypeError
        return 0
