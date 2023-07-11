# Implementation of Variable size Huffman Coding Tree
from __future__ import annotations

from collections import Counter
from typing import Any, Optional, Union

from datastax.Arrays import PriorityQueue
from datastax.trees.private_trees import huffman_tree
from datastax.trees.private_trees.huffman_tree import HuffmanNode


class HuffmanTable(huffman_tree.HuffmanTable):
    def _calculate_size(self):
        size = 0
        for char, huff_code in self.data.items():
            size += ord(char).bit_length() + len(huff_code)
        self._size = size


class HuffmanTree(huffman_tree.HuffmanTree):
    def _construct(self, data: Union[list[str], str] = None
                   ) -> Optional[HuffmanTree]:
        if not data or data[0] is None:
            return None

        def comparator(n1: HuffmanNode, n2: HuffmanNode) -> HuffmanNode:
            if n1.frequency > n2.frequency:
                return n2
            return n1

        nodes = (
            HuffmanNode(
                _data, None, None, frequency
            ) for _data, frequency in Counter(data).items()
        )
        p_queue = PriorityQueue(capacity=None, custom_comparator=comparator)
        for node in nodes:
            p_queue.enqueue(node)

        while len(p_queue.array) >= 2:
            node1 = p_queue.dequeue()
            node2 = p_queue.dequeue()
            root_freq = sum((node1.frequency, node2.frequency))
            root = HuffmanNode(None, node1, node2, root_freq)
            p_queue.enqueue(root)

        self._root = p_queue.dequeue()
        self._calculate_huffman_code()
        self._create_huffman_table()
        return self

    def huffman_code_of(self, character: str) -> Optional[str]:
        def find(node: HuffmanNode, path=None):
            if not node:
                return None
            path = path or []
            if node.data == character:
                return path
            path.append(0)
            if find(node.left, path) is not None:
                return path
            path.pop()
            path.append(1)
            if find(node.right, path) is not None:
                return path
            path.pop()

        result = find(self.root)
        return ''.join(map(str, result)) if result else None

    # Private method to build data dictionary for HuffmanTable
    def _create_huffman_table(self):
        items = {}
        for item in self._data:
            items[item] = self.huffman_code_of(item)
        self._table = HuffmanTable(items, Counter(self._data))

    def _calculate_huffman_code(self):
        self._huffman_code = ''.join(
            self.huffman_code_of(character) for character in self._data
        )
        pass

    def size_calculator(self) -> Optional[tuple[int, int]]:
        """
        Calculates the actual encoding size and total
        huffman encoding size with table included
        """
        if not self.root or not self.huffman_table:
            return None
        fixed_encoding = huffman_encoding = 0
        frequency = self.huffman_table.frequency

        for char, huff_code in self.huffman_table.data.items():
            # Converting item to ascii finding bit_length and multiplying
            # it with frequency
            total_bit_length = ord(char).bit_length() * frequency[char]
            fixed_encoding += total_bit_length  # Adding to fixed_encoding

            # Already in Binary so no conversion to ascii
            total_bit_length = len(huff_code) * frequency[char]
            huffman_encoding += total_bit_length  # Adding to huffman_encoding

        return fixed_encoding, huffman_encoding + self.huffman_table.size

    def compression_ratio(self) -> Optional[str]:
        if not self.root:
            return None
        result = self.size_calculator()
        if not result:
            return None
        fixed_encoding, huffman_encoding = result
        compression_ratio = huffman_encoding / fixed_encoding
        return f"{compression_ratio :.2%}"

    def space_saved(self) -> Optional[str]:
        if not self.root:
            return None
        result = self.size_calculator()
        if not result:
            return None
        fixed_encoding, huffman_encoding = result
        space_saved = (fixed_encoding - huffman_encoding) / fixed_encoding
        return f"{space_saved :.2%}"

    @staticmethod
    def decode_from_table(huffman_code: str,
                          huffman_table: dict[str, str]) -> str:
        huffman_table = {code: char for char, code in huffman_table.items()}
        decoded_message = ''
        per_character = ''
        for item in huffman_code:
            if per_character in huffman_table:
                decoded_message += huffman_table[per_character]
                per_character = ''
            per_character += item
        return decoded_message

    def insert(self, item: Any):
        raise NotImplementedError
