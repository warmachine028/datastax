from typing import Any

from datastax.trees import BinarySearchTree


def test(array: list[Any]):
    bst = BinarySearchTree(array)
    print(bst)
    print(bst.preorder_print())
    print(bst.array_repr)


test([None, 1])
test([1, 1, 1])
test([1, 2, 3, None, 5])
test([1, 2, 3, 4])
test([4, 4, 4, 4, 3, ['1']])
test([4, 3, 1, 8, 9, 10])
test(["1", "B", "Baxy", "D"])
test([BinarySearchTree([10, 20, 30]), BinarySearchTree([10])])
test([(10, 20), [10, 20]])
test([{1, 2, 3}, {2, 3}, {4, 6, 5}])
test([3, 1, 2, 4, 5, 9, 0, -4, -3])
