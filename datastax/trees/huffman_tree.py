from __future__ import annotations

from collections import Counter
from typing import Any, Optional, Union

from datastax.arrays import PriorityQueue
from datastax.trees.private_trees import huffman_tree
from datastax.trees.private_trees.huffman_tree import HuffmanNode


class HuffmanTree(huffman_tree.HuffmanTree):
    def __init__(self, string: Union[list, str] = None):
        self.string = string
        self._huffman_code = None
        super().__init__(string)

    def insert(self, item: Any):
        raise NotImplementedError

    def _construct(self, string: Union[list, str] = None
                   ) -> Optional[HuffmanTree]:
        if not string or string[0] is None:
            return None

        def comparator(n1: HuffmanNode, n2: HuffmanNode) -> HuffmanNode:
            if n1.frequency > n2.frequency:
                return n2
            return n1

        nodes = [
            HuffmanNode(
                data, None, None, frequency
            ) for data, frequency in Counter(string).items()
        ]
        p_queue = PriorityQueue(None, comparator)
        for node in nodes:
            p_queue.enqueue(node)

        while not p_queue.is_empty():
            print([node.frequency for node in p_queue.array])
            print(p_queue.peek())
            node1 = p_queue.dequeue()
            if p_queue.is_empty():
                break
            node2 = p_queue.dequeue()
            root_freq = sum((node1.frequency, node2.frequency))
            root = HuffmanNode(None, node1, node2, root_freq)
            print(root)
            p_queue.enqueue(root)
            self._root = p_queue.array[0]

        self._calculate_huffman_code()
        return self

    @property
    def huffman_code(self):
        return self._huffman_code

    def _calculate_huffman_code(self):
        result = ''
        self._huffman_code = result
        pass

    def compression_ratio(self):
        pass
