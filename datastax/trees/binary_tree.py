# Binary Tree Implementation
from __future__ import annotations

import warnings
from typing import Any, Optional

from datastax.errors import (
    PathNotGivenError,
    PathNotFoundError,
    PathAlreadyOccupiedWarning,
    NodeNotFoundWarning,
    DeletionFromEmptyTreeWarning,
)
from datastax.Lists import Queue
from datastax.trees.private_trees import binary_tree
from datastax.trees.private_trees.binary_tree import TreeNode


class BinaryTree(binary_tree.BinaryTree):
    def insert_path(self, data: Any, path: list[str] = None) -> None:
        node = TreeNode(data)
        if not self._root:
            self._root = node
            return
        if not path:
            raise PathNotGivenError(self)
        parent = self._root
        for direction in path[:-1]:  # Reaching
            if direction == 'left' and parent.left:
                parent = parent.left
            elif direction == 'right' and parent.right:
                parent = parent.right
            else:
                raise PathNotFoundError(self)
        if path[-1] == 'right' and not parent.right:
            parent.right = node
        elif path[-1] == 'left' and not parent.left:
            parent.left = node
        else:
            occupied_node = parent.left if path[-1] == 'left' else parent.right
            warnings.warn("Insertion unsuccessful. Path already occupied by "
                          f"TreeNode [{occupied_node.data}]",
                          PathAlreadyOccupiedWarning)

    # Helper function to construct tree by level order -> Array to tree
    def _construct(self, array: list[Any] = None) -> Optional[BinaryTree]:
        if not array or array[0] is None:
            return None

        queue = Queue(capacity=len(array))
        current = 0
        root = self.root
        if not root:
            root = TreeNode(array[0])
            current = 1
        queue.enqueue(root)
        while not queue.is_empty() and current < len(array):
            node = queue.dequeue()
            node.left = None if array[current] is None else TreeNode(
                array[current])
            if node.left:
                queue.enqueue(node.left)  # Inserting Left Node
            current += 1
            if current >= len(array):
                break
            node.right = None if array[current] is None else TreeNode(
                array[current])
            if node.right:
                queue.enqueue(node.right)  # Inserting Right Node
            current += 1
        self._root = root
        return self

    def delete(self, data: Any = None) -> Optional[Any]:
        """
        Deletes a node which has the data and replaces with RightMost Leaf Node
        :param data: An item corresponding to the node to be deleted
        :return: returns data if node is found else None and raises warning
        """
        if not self.root or data is None:
            return self.delete_deepest()

        queue = Queue(capacity=len(self.array_repr))
        queue.enqueue(self.root)
        del_node = None
        while not queue.is_empty():
            node = queue.dequeue()
            if node.data == data:
                del_node = node
                break
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        del_data = None
        if del_node:
            leaf_data = self.delete_deepest()
            if leaf_data is not None:
                del_data, del_node.data = del_node.data, leaf_data
        else:
            warnings.warn(
                "Deletion unsuccessful. Node was not found with current "
                f"data '{data}'", NodeNotFoundWarning
            )
        return del_data

    def delete_deepest(self) -> Optional[Any]:
        """
        Deletes the rightmost leaf node
        :return: data if tree is not empty else None
        """
        queue = Queue(capacity=len(self.array_repr))
        if self.root:
            queue.enqueue(self.root)
        parent = None
        while not queue.is_empty():
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
                if not any([node.left.left, node.left.right]):
                    parent = node
            if node.right:
                queue.enqueue(node.right)
                if not any([node.right.left, node.right.right]):
                    parent = node

        data = None
        if parent:
            if parent.right:
                data = parent.right.data
                parent.right = None
            else:
                data = parent.left.data
                parent.left = None
        elif self._root:
            data = self._root.data
            self._root = None
        else:
            warnings.warn(
                "Deletion Unsuccessful. Can't delete from empty Tree",
                DeletionFromEmptyTreeWarning
            )
        return data

    def insert(self, item: Any):

        temp = None if item is None else TreeNode(item)
        queue = Queue(capacity=len(self.array_repr))
        if self.root:
            queue.enqueue(self.root)
        while not queue.is_empty():
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            else:
                node.left = temp
                return
            if node.right:
                queue.enqueue(node.right)
            else:
                node.right = temp
                return
        else:
            self._root = temp
