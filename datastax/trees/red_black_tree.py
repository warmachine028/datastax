# Implementation of Variable size Huffman Coding Tree
from __future__ import annotations

import warnings
from typing import Optional

from datastax.errors import (
    DuplicateNodeWarning
)
from datastax.trees.binary_search_tree import BinarySearchTree
from datastax.trees.private_trees import red_black_tree
from datastax.trees.private_trees.red_black_tree import RedBlackNode


class RedBlackTree(BinarySearchTree,
                   red_black_tree.RedBlackTree,
                   ):  # Private helper function for inserting
    def _place(self, parent, data) -> Optional[RedBlackNode]:
        if not parent:
            return RedBlackNode(data)
        elif parent.data < data:
            parent.right = self._place(parent.right, data)
        elif parent.data > data:
            parent.left = self._place(parent.left, data)
        else:
            warnings.warn(
                f"Insertion unsuccessful. Item '{data}' already exists "
                "in Tree", DuplicateNodeWarning)
        return parent


if __name__ == '__main__':
    rbt = RedBlackTree([1, 2, 3, 4])
    print(BinarySearchTree([1, 2, 3, 4]))
    print(rbt)
