import warnings
from typing import Any, Optional, Self, Sequence
from datastax.Utils.Warnings import DuplicateNodeWarning
from datastax.Lists import Queue
from datastax.Trees.BinaryTree import BinaryTree
from datastax.Trees.AbstractTrees import ThreadedBinaryTree as AbstractTree
from datastax.Nodes import ThreadedNode


class ThreadedBinaryTree(BinaryTree, AbstractTree):
    dummy_node = ThreadedNode(None)
    tail: Optional[ThreadedNode] = None
    head: Optional[ThreadedNode] = None

    def set_root(self, root):
        if root is None or isinstance(root, ThreadedNode):
            super().set_root(root)
            self.head = self.tail = self.root
            self.dummy_node.set_left(self.root)
            self.dummy_node.set_right(self.dummy_node)
            return
        raise TypeError("The 'root' parameter must be an "
                        "instance of ThreadedNode or its subclass.")

    def _construct(self, items: Optional[Sequence] = None) -> Self | None:
        if not items or items[0] is None:
            return None
        for item in items:
            self.insert(item)
        return self

    @property  # Level Order Traversal -> Tree to array
    def array_repr(self) -> list[Any]:
        array = []
        queue = Queue()
        if self.root:
            queue.enqueue(self.root)
        while not queue.is_empty():
            node = queue.dequeue()
            array.append(node.data)
            if node.left_is_child:
                queue.enqueue(node.left)
            if node.right_is_child:
                queue.enqueue(node.right)

        return array

    def convert_from(self, root: Any) -> None:
        def insert_inorder(node: ThreadedNode | None) -> None:
            if not node:
                return
            insert_inorder(node.left)
            array.append(node)
            insert_inorder(node.right)

        def clone_binary_tree(node) -> Optional[ThreadedNode]:
            if not node:
                return None
            return ThreadedNode(node.data,
                                clone_binary_tree(node.left),
                                clone_binary_tree(node.right))

        array: list[ThreadedNode] = []
        self.set_root(clone_binary_tree(root))

        # Storing inorder traversal in queue
        insert_inorder(self.root)
        for n in range(len(array)):
            if not array[n].left:
                array[n].set_left(
                    self.dummy_node if not n else array[n - 1]
                )
            if not array[n].right:
                array[n].set_right(
                    self.dummy_node if n == len(array) - 1 else array[n + 1]
                )

        self.head, self.tail = array[0], array[-1]
        self.dummy_node.set_left(self.root)
        self.dummy_node.set_left_is_child(True)

    def insert(self, data: Any, root: Optional[ThreadedNode] = None) -> None:
        root = root or self.root
        if not root:
            node = ThreadedNode(data, self.dummy_node, self.dummy_node)
            node.set_left_is_child(False)
            node.set_right_is_child(False)
            self.set_root(node)
            self.head = self.tail = self.root
            self.dummy_node.set_left(self.root)
            self.dummy_node.set_left_is_child(True)
            return

        node = ThreadedNode(data)
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
            node.set_left(root.left)
            root.set_left(node)
            node.set_left_is_child(root.left_is_child)
            root.set_left_is_child(True)
            node.set_right(root)

        elif right and root:
            node.set_right(root.right)
            root.set_right(node)
            node.set_right_is_child(root.right_is_child)
            root.set_right_is_child(True)
            node.set_left(root)

        if node.left is self.dummy_node:
            self.head = node
        elif node.right is self.dummy_node:
            self.tail = node

    # DFS Traversal without using stack
    def inorder(self) -> list[Any]:
        ref = self.head
        array = []
        while ref and ref is not self.dummy_node:
            array.append(ref.data)
            if not ref.right_is_child:
                ref = ref.right
            else:
                node = ref.right
                while node.left_is_child:
                    node = node.left
                ref = node
        return array


if __name__ == '__main__':
    T = ThreadedBinaryTree([10, 30], ThreadedNode(20))
    print(T)
    # print(T.root)
    # print(T.root.left)
    # print(T.root.right is T.dummy_node)
    T.insert(110)
    print(T)
    print(ThreadedBinaryTree([110, 10, 20]))
