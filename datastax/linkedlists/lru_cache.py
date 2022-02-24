"""
Implementation of LRU Cache using DoublyLinkedList and HashMap
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise
return -1.
- void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds
the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

LRU -> Least Recently used
"""
from typing import Any

from datastax.linkedlists import DoublyLinkedList, DoublyNode


class LRUCache(DoublyLinkedList):
    def __init__(self, capacity: int):
        super().__init__()
        self._capacity = capacity
        self._cache: dict[int, DoublyNode] = {}
        self._head = DoublyNode('HEAD')
        self._tail = DoublyNode('TAIL')
        self.tail.prev = self.head
        self.head.next = self.tail

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        node = self._cache[key]
        self._enqueue(node)
        return node.data[1]

    def put(self, key: int, value: int) -> None:
        if key not in self._cache:
            node = DoublyNode([key, value])
            if len(self._cache) == self._capacity:
                self._dequeue()
        else:
            node = self._cache[key]
            node.data[1] = value
        self._enqueue(node)

    def _enqueue(self, node: DoublyNode) -> None:
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self._cache[node.data[0]] = node

    def _dequeue(self) -> None:
        node = self.head.next
        self.head.next = node.next
        node.next.prev = node.prev
        self._cache.pop(node.data[0])

    def append(self, data) -> None:
        raise NotImplementedError

    def insert(self, data: Any):
        return NotImplementedError
