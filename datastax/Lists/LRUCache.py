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

from datastax.Lists.DoublyLinkedList import DoublyLinkedList
from datastax.Lists.DoublyNode import DoublyNode


class LRUCache(DoublyLinkedList):
    def __init__(self, capacity: int):
        super().__init__()
        self._capacity = capacity
        self._cache: dict[int, DoublyNode] = {}
        self._head = DoublyNode('HEAD')
        self._tail = DoublyNode('TAIL')
        self.tail.set_prev(self.head)
        self.head.set_next(self.tail)

    def get(self, key: int) -> int | None:
        if key not in self._cache:
            return -1
        node = self._cache[key]
        self._enqueue(node)
        return node.data[1] if node.data else None

    def put(self, key: int, value: int):
        if key not in self._cache:
            node = DoublyNode([key, value])
            if len(self._cache) == self._capacity:
                self._dequeue()
        else:
            node = self._cache[key]
            if node.data:
                node.data[1] = value
        self._enqueue(node)

    def _enqueue(self, node: DoublyNode):
        if node.prev:
            node.prev.set_next(node.next)
        if node.next:
            node.next.set_prev(node.prev)
        node.set_prev(self.tail.prev)
        node.set_next(self.tail)
        self.tail.prev.set_next(node)
        self.tail.set_prev(node)
        if node.data:
            self._cache[node.data[0]] = node

    def _dequeue(self) -> None:
        node = self.head.next
        self.head.set_next(node.next)
        node.next.set_prev(node.prev)
        self._cache.pop(node.data[0])

    def append(self, data) -> None:
        raise NotImplementedError

    def insert(self, data: Any):
        return NotImplementedError
