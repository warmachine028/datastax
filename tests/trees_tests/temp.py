from datastax.linkedlists import Queue
from datastax.trees import ThreadedBinaryTree, ThreadedTreeNode


def level_wise_items(tree) -> list:
    result = []
    queue: Queue = Queue()
    if tree.root:
        queue.enqueue(tree.root)
    while not queue.is_empty():
        node: ThreadedTreeNode = queue.dequeue()
        result.append(node.data)
        if node.left_is_child:
            queue.enqueue(node.left)
        if node.right_is_child:
            queue.enqueue(node.right)
    return result


x = ThreadedBinaryTree([{1, 2, 3},
                        [1, 2, 3, 4, 5],
                        ["1", "2"],
                        {1: 2, 3: 4, 5: 6},
                        "STRING",
                        'c'])
ar = level_wise_items(x)
print(ar)
