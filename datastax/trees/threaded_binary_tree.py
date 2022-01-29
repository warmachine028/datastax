# Threaded Binary Tree Implementation
from __future__ import annotations

import warnings
from typing import Optional, Any, Union

from datastax.errors import DuplicateNodeWarning, ExplicitInsertionWarning
from datastax.trees import TreeNode, AVLNode, HeapNode
from datastax.trees.private_trees import threaded_binary_tree
from datastax.trees.private_trees.threaded_binary_tree import ThreadedNode

rootNode = Union[TreeNode, AVLNode, HeapNode]


class ThreadedBinaryTree(threaded_binary_tree.ThreadedBinaryTree):
    def convert_to_tbt(self, root: rootNode) -> None:
        def insert_inorder(node: Optional[ThreadedNode]) -> None:
            if not node:
                return
            insert_inorder(node.left)
            array.append(node)
            insert_inorder(node.right)

        def clone_binary_tree(node: rootNode) -> Optional[ThreadedNode]:
            if not node:
                return None
            return ThreadedNode(node.data,
                                clone_binary_tree(node.left),
                                clone_binary_tree(node.right))

        array: list[ThreadedNode] = []
        self._root = clone_binary_tree(root)

        # Storing inorder traversal in queue
        insert_inorder(self._root)
        for n in range(len(array)):
            if not array[n].left:
                array[n].left = self.dummy_node if not n else array[n - 1]
            if not array[n].right:
                array[n].right = self.dummy_node if n == len(array) - 1 \
                    else array[n + 1]

        self.head, self.tail = array[0], array[-1]
        self.dummy_node.left = self.root
        self.dummy_node.left_is_child = True

    def insert(self, data: Any, root: ThreadedNode = None) -> None:
        if not isinstance(self.tree, ThreadedBinaryTree):
            warnings.warn(
                "Can't insert in Threaded Tree with explicit insertion logic"
                "of Foreign Tree Logic",
                ExplicitInsertionWarning
            )
            return
        root = root or self.root
        node = ThreadedNode(data)
        if not root:
            self._root = node
            node.left = node.right = self.dummy_node
            self.head = self.tail = self.root
            self.dummy_node.left = self.root
            self.dummy_node.left_is_child = True
            return

        left = right = False
        while root:
            if data is None:
                break
            if root.data > data:
                if not root.left_is_child:
                    # will insert the child as left child
                    left = True
                    break
                else:
                    root = root.left
            elif root.data < data:
                if not root.right_is_child:
                    # will insert the child as right child
                    right = True
                    break
                else:
                    root = root.right
            else:
                warnings.warn(
                    f"Insertion unsuccessful. Item '{data}' already exists "
                    "in Tree", DuplicateNodeWarning)
                return

        if left and root:
            node.left = root.left
            root.left = node
            node.left_is_child = root.left_is_child
            root.left_is_child = True
            node.right = root

        elif right and root:
            node.right = root.right
            root.right = node
            node.right_is_child = root.right_is_child
            root.right_is_child = True
            node.left = root

        if node.left is self.dummy_node:
            self.head = node
        elif node.right is self.dummy_node:
            self.tail = node

    # DFS Traversal without using stack
    def inorder(self) -> list[Any]:
        ref: ThreadedNode = self.head
        array: list[Any] = []
        while ref is not self.dummy_node:
            array.append(ref.data)
            if not ref.right_is_child:
                ref = ref.right
            else:
                node = ref.right
                while node.left_is_child:
                    node = node.left
                ref = node
        return array
