import warnings
from typing import Any, Optional, Self, Sequence
from datastax.Utils.Exceptions import (
    PathNotGivenException,
    PathNotFoundException,
)
from datastax.Utils.Warnings import (
    PathAlreadyOccupiedWarning,
    NodeNotFoundWarning,
    DeletionFromEmptyTreeWarning,
)
from datastax.Lists import Queue
from datastax.Nodes import TreeNode
from datastax.Trees.AbstractTrees import BinaryTree as AbstractTree


class BinaryTree(AbstractTree):
    def __init__(self, items: Optional[Sequence] = None,
                 root: Optional[TreeNode] = None):
        self.set_root(root)
        self._construct(items)
        self._string: Optional[str] = None

    def set_root(self, root: TreeNode | None):
        if root is None or isinstance(root, TreeNode):
            self._root = root
            return
        raise TypeError("The 'root' parameter must be an "
                        "instance of TreeNode or its subclass.")

    def insert_path(self, data: Any, path: Optional[list[str]] = None) -> None:
        node = TreeNode(data)
        if not self._root:
            self._root = node
            return
        if not path:
            raise PathNotGivenException(self)
        parent = self._root
        for direction in path[:-1]:  # Reaching
            if direction == 'left' and parent.left:
                parent = parent.left
            elif direction == 'right' and parent.right:
                parent = parent.right
            else:
                raise PathNotFoundException(self)
        if path[-1] == 'right' and not parent.right:
            parent.set_right(node)
        elif path[-1] == 'left' and not parent.left:
            parent.set_left(node)
        else:
            occupied_node = parent.left if path[-1] == 'left' else parent.right
            warnings.warn("Insertion unsuccessful. Path already occupied by "
                          f"TreeNode [{occupied_node.data}]",
                          PathAlreadyOccupiedWarning)

    # Helper function to construct tree by level order -> Array to tree
    def _construct(self, items: Optional[Sequence] = None) -> Self | None:
        if not items or items[0] is None:
            return None

        queue = Queue(capacity=len(items))
        current = 0
        root = self.root
        if not root:
            root = TreeNode(items[0])
            current = 1
        queue.enqueue(root)
        while not queue.is_empty() and current < len(items):
            node = queue.dequeue()
            node.set_left(None if items[current] is None else TreeNode(
                items[current]))
            if node.left:
                queue.enqueue(node.left)  # Inserting Left Node
            current += 1
            if current >= len(items):
                break
            node.set_right(None if items[current] is None else TreeNode(
                items[current]))
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
                parent.set_right(None)
            else:
                data = parent.left.data
                parent.set_left(None)
        elif self._root:
            data = self._root.data
            self.set_root(None)
        else:
            warnings.warn(
                "Deletion Unsuccessful. Can't delete from empty Tree",
                DeletionFromEmptyTreeWarning
            )
        return data

    def insert(self, item: Any) -> None:
        temp = None if item is None else TreeNode(item)
        queue = Queue(capacity=len(self.array_repr))
        if self.root:
            queue.enqueue(self.root)
        while not queue.is_empty():
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            else:
                node.set_left(temp)
                return
            if node.right:
                queue.enqueue(node.right)
            else:
                node.set_right(temp)
                return
        else:
            self._root = temp
