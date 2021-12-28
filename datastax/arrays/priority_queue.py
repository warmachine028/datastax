# Priority Queue implementation using Lists (Pseudo Arrays)
from typing import Any

from datastax.arrays.queue import Queue
from datastax.errors import OverFlowError, UnderFlowError


class PriorityQueue(Queue):
    def heapify(self, index: int, length: int) -> None:
        root = index
        left_child = root * 2 + 1
        right_child = root * 2 + 2
        if left_child < length and self.array[left_child] > self.array[root]:
            root = left_child
        if right_child < length and self.array[right_child] > self.array[root]:
            root = right_child
        if root == index: return
        self._array[root], self._array[index] = self.array[index], self.array[root]
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
            self.heapify(i, n)
        return 0


if __name__ == '__main__':
    pq = PriorityQueue(5)
    # print()
    pq.enqueue(10)
    pq.enqueue(20)
    pq.enqueue(15)
    pq.enqueue(30)
    pq.enqueue(40)
    print(pq)
    pq.enqueue(-5)
    print(pq)
    pq.enqueue(90)
    for i in range(10):
        x = pq.dequeue()
        print(f"Popped Element: {x}")
        print(pq)
    print(pq)
