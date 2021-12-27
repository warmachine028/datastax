# Max Heap Tree Implementation
from __future__ import annotations

from typing import Optional, Any

from datastax.trees.binary_tree import BinaryTree


class MaxHeapTree(BinaryTree):
    def __init__(self, array: list[Any] = None, root=None):
        self.heap: list[Any] = []
        super().__init__(array, root)
    
    def array_repr(self) -> list[Any]:
        return self.heap
    
    def _construct(self, array: list[Any] = None) -> Optional[MaxHeapTree]:
        if not array or array[0] is None: return None
        for item in array:
            try:
                self.heappush(item)
            except TypeError as error:
                print(error)
                break
        return self
    
    def _shift_up(self, heap: list[Any], index: int, length: int) -> None:
        root = index
        left_child = root * 2 + 1
        right_child = root * 2 + 2
        if left_child < length and heap[left_child] > heap[root]:
            root = left_child
        if right_child < length and heap[right_child] > heap[root]:
            root = right_child
        if root == index: return
        heap[root], heap[index] = heap[index], heap[root]
        self._shift_up(heap, root, length)
    
    def heapify(self, array: list[Any]) -> None:
        for item in array:
            self.heappush(item)
    
    def heappop(self, heap: list[Any] = None) -> Optional[Any]:
        if not heap: heap = self.heap
        if not heap: return None
        deleted_item = heap[0]
        heap[0] = heap.pop()
        self._shift_up(heap, 0, len(heap))
        if heap: super()._construct(heap)
        else: self._root = None
        return deleted_item
    
    def heappush(self, item: Any, heap: list[Any] = None) -> None:
        if heap is None: heap = self.heap
        heap.append(item)
        for i in range(len(heap) - 1, -1, -1):
            self._shift_up(heap, i, len(heap))
        super()._construct(heap)
