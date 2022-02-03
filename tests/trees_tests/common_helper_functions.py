from typing import Any

from datastax.linkedlists import Queue


def level_wise_items(tree) -> list:
    result = []
    queue: Queue = Queue()
    if tree.root:
        queue.enqueue(tree.root)
    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node.data)
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    return result


def inorder_items(tree) -> list:
    def inorder(root) -> None:
        if root:
            inorder(root.left)
            result.append(root.data)
            inorder(root.right)

    result: list = []
    inorder(tree.root)
    return result


def postorder_items(tree) -> list:
    def postorder(root) -> None:
        if root:
            postorder(root.left)
            postorder(root.right)
            result.append(root.data)

    result: list = []
    postorder(tree.root)
    return result


def max_heapify(test_case: list[Any]) -> list[Any]:
    heap: list[Any] = []

    def heapify(index):
        root = index
        left_child, right_child = root * 2 + 1, root * 2 + 2
        if left_child < n and heap[left_child] > heap[root]:
            root = left_child
        if right_child < n and heap[right_child] > heap[root]:
            root = right_child
        if root != index:
            heap[index], heap[root] = heap[root], heap[index]
            heapify(root)

    if not test_case or test_case[0] is None:
        return heap
    for i, item in enumerate(filter(lambda x: x is not None, test_case)):
        heap.append(item)
        n = len(heap)
        for j in range(n // 2 - 1, -1, -1):
            heapify(j)

    return heap


def check_bst_property(node) -> bool:
    """
    :param node: Root of red black Tree
    :return: True if Tree is a valid BST else False
    """
    if not node:  # Reached its Leaf node
        return True
    if node.left and node.left.data > node.data:  # left must be < node
        return False
    if node.right and node.data > node.right.data:  # right must be > node
        return False
    # Recursively checking for left and right subtrees
    return check_bst_property(node.left) and check_bst_property(node.right)
