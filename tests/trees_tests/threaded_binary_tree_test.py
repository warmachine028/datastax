import random
import string
import unittest
from typing import Optional, Any

from datastax.errors import DuplicateNodeWarning, ExplicitInsertionWarning
from datastax.linkedlists import Queue
from datastax.trees import ThreadedBinaryTree, ThreadedNode


class TestThreadedBinaryTree(unittest.TestCase):

    def setUp(self) -> None:
        self.tbt = ThreadedBinaryTree()
        self.test_cases = 10
        self.max_sample_size = 10
        self.items = [1, 3, 2, 4, 5, 33, 22]
        self.print_test_cases = [
            [1],
            [None, 10],
            [10, None, None],
            ['root', None, None, 'child'],
            [4, 4, 4, 4, 3, ['1']],
            [(10, 20), [10, 20]],
            [1, None, 2, 3, None, None, 4, 5]
        ]

    def test_array_representation(self):
        testcases = [
            [*range(10)],
            [None, 10],
            [10, None, None],
            ['root', None, None, 'child']
        ]
        results = [
            [*range(10)],
            [],
            [10],
            ['root', 'child']
        ]
        for testcase, result in zip(testcases, results):
            tree = ThreadedBinaryTree(testcase)
            self.assertEqual(result, tree.array_repr)

    def test_avl_tree(self):
        # testing insertion
        data = [4, 3, 1, 2, 5, 9]
        result = [3, 1, 5, 2, 4, 9]
        # Normal inserting
        tree = ThreadedBinaryTree(data, "AVLTree")
        self.assertEqual(result, self.level_wise_items(tree))
        self.assertEqual(result, tree.array_repr)
        self.assertEqual(sorted(result), tree.inorder())
        # Testing Dummy Node
        self.assertEqual(tree.dummy_node.left.data, 3)  # root
        self.assertEqual(tree.dummy_node.right, tree.dummy_node)

        with self.assertWarns(ExplicitInsertionWarning):
            tree.insert(10)

    def test_construction(self):
        items = [
            [1, 2, 3, 4, 5, 6],  # <- Using general list of ints
            [*range(10)],  # <- Using range object unpacking in list
            [],  # <- Using Empty list
            [None],  # <- Using only None item passed through list
            [None, 1, 2, 3, 4, 5],  # <- Using First item as None
            None,  # <- Using None passed directly
        ]
        results = [
            [[1, 2, 3, 4, 5, 6], 1],
            [[*range(10)], 0],
            [[], None],
            [[], None],
            [[], None],
            [[], None]
        ]
        for item, result in zip(items, results):
            tree = ThreadedBinaryTree(item)
            # checking tree items
            self.assertEqual(result[0], tree.array_repr)
            # checking root
            self.assertEqual(result[1], tree.root.data if tree.root else None)

        # Construct with existing root
        root_node = ThreadedNode(10)
        tree = ThreadedBinaryTree([*range(9, 0, -1)], None, root_node)
        self.assertEqual([*range(10, 0, -1)], tree.array_repr)

    def test_heap_trees(self):
        # First Max Heap
        data = [4, 3, 1, 2, 5, 3, 2, 1, 9]
        result = [9, 5, 3, 4, 3, 1, 2, 1, 2]
        # Normal inserting
        tree = ThreadedBinaryTree(data, "HeapTree")
        self.assertEqual(result, self.level_wise_items(tree))
        self.assertEqual(result, tree.array_repr)
        self.assertEqual(self.inorder(tree), tree.inorder())
        # # Testing Dummy Node
        self.assertEqual(tree.dummy_node.left.data, 9)  # root
        self.assertEqual(tree.dummy_node.right, tree.dummy_node)

        with self.assertWarns(ExplicitInsertionWarning):
            tree.insert(10)

    def test_insert(self):
        self.assertEqual([], self.level_wise_items(self.tbt))

        # testing insertion
        data = [4, 3, 1, 2, 5, 3, 2, 1, 9]
        results = [
            [4],
            [4, 3],
            [4, 3, 1],
            [4, 3, 1, 2],
            [4, 3, 5, 1, 2],
            [4, 3, 5, 1, 9, 2]
        ]
        # Normal inserting
        for item, result in zip(data[:5], results[:5]):
            self.tbt.insert(item)
            self.assertEqual(result, self.level_wise_items(self.tbt))

        # Testing warnings
        for item in data[5:-1]:
            with self.assertWarns(DuplicateNodeWarning):
                self.tbt.insert(item)

    def test_insert_with_logic(self):
        # Inserting with explicit insertion logic of same type
        tree = ThreadedBinaryTree(self.items, "ThreadedBinaryTree")
        self.traversal_testing(tree, self.items)
        # Testing Dummy Node
        self.assertEqual(tree.dummy_node.left.data, 1)
        self.assertEqual(tree.dummy_node.right, tree.dummy_node)

        tree = ThreadedBinaryTree(self.items, "BinarySearchTree")
        self.traversal_testing(tree, self.items)
        # Testing Dummy Node
        self.assertEqual(tree.dummy_node.left.data, 1)
        self.assertEqual(tree.dummy_node.right, tree.dummy_node)

    def test_inserting_heterogeneous_items(self):
        # inserting miscellaneous items
        items = [
            {1: 2, 2: 3, 3: 4},  # -> dictionary
            {1, 2, 3, 4, 5, 6, 7},  # -> set
            [1, 2, 3, 4, 5],  # -> list
            1234567890,  # -> integer
            "string",  # -> string
            'A',  # -> char
            # Inserting Uncommon items
            ThreadedBinaryTree([1, 2]).root,  # -> Node
            ThreadedBinaryTree([1, 2]),  # ->  self referential type
            None  # -> * can't be inserted anywhere
            # entire list will be discarded if Node as first element
        ]
        # Must Raise Type Error in normal insertion
        with self.assertRaises(TypeError):
            ThreadedBinaryTree(items)

        # Would be able to build successfully
        tree = ThreadedBinaryTree(items, 'BinaryTree')
        self.assertEqual(items[:-1], self.level_wise_items(tree))

    def test_normal_binary_tree_construction(self):
        tree = ThreadedBinaryTree(self.items, "BinaryTree")
        self.assertEqual(self.items, self.level_wise_items(tree))
        self.assertEqual(self.items, tree.array_repr)
        self.assertEqual(self.inorder(tree), tree.inorder())
        # Testing Dummy Node
        self.assertEqual(tree.dummy_node.left.data, 1)
        self.assertEqual(tree.dummy_node.right, tree.dummy_node)

        with self.assertWarns(ExplicitInsertionWarning):
            tree.insert(10)

    def test_preorder_print(self):
        results = [
            '\n1', 'NULL', '\n10', '\nroot'
                                   '\n└─▶ child',
            '\n4'
            '\n├─▶ 4'
            '\n│   ├─▶ 4'
            '\n│   └─▶ 3'
            '\n└─▶ 4'
            '\n    └─▶ [\'1\']',

            '\n(10, 20)'
            '\n└─▶ [10, 20]',

            '\n1'
            '\n└─▶ 2'
            '\n    └─▶ 3'  # An example of a right skewed tree
            '\n        └─▶ 4'
            '\n            └─▶ 5'
        ]

        for testcase, result in zip(self.print_test_cases[:-3] +
                                    self.print_test_cases[-1:],
                                    results[:-3] + results[-1:]):
            tree = ThreadedBinaryTree(testcase)
            tree.preorder_print()
            self.assertEqual(result, tree._string)

        for testcase, result in zip(self.print_test_cases[-3:-1],
                                    results[-3:-1]):
            tree = ThreadedBinaryTree(testcase, 'BinaryTree')
            tree.preorder_print()
            self.assertEqual(result, tree._string)

    def test_string_representation(self):
        results = [
            '\n        ┌┐'
            '\n   ┌>DU..│<┐'
            '\n   │   ┌┴┘ │'
            '\n   │   1   │'
            '\n   └───┴───┘',

            '  NULL', '\n        ┌┐'
                      '\n   ┌>DU..│<┐'
                      '\n   │   ┌┴┘ │'
                      '\n   │   10  │'
                      '\n   └───┴───┘',
            '\n                            ┌───┐'
            '\n     ┌──────────────────> DUMMY │<─┐'
            '\n     │                  ┌───┴───┘  │'
            '\n     │                root         │'
            '\n     │     ┌───────────┴───────────┘'
            '\n     │   child   │'
            '\n     └─────┴─────┘',

            '\n                                ┌───┐'
            '\n      ┌─────────────────────> DUMMY │<───┐'
            '\n      │                     ┌───┴───┘    │'
            '\n      │                 (10, 20)         │'
            '\n      │      ┌─────────────┴─────────────┘'
            '\n      │   [10, 20]  │'
            '\n      └──────┴──────┘'

        ]
        for testcase, result in zip(self.print_test_cases, results[:4]):
            tree = ThreadedBinaryTree(testcase)
            self.assertEqual(result, tree.__str__())
        tree = ThreadedBinaryTree(self.print_test_cases[5], "BinaryTree")
        self.assertEqual(results[-1], tree.__str__())

    def test_with_random_inputs(self):
        numbers = range(-100, 100)
        characters = string.ascii_uppercase + string.ascii_lowercase
        # To avoid terminal explosion please avoid printing these trees
        # after construction
        for _ in range(self.test_cases):
            sample_size = random.randint(1, self.max_sample_size)
            sample = random.sample(numbers, sample_size)

            # Constructing tree with random numbers
            tree = ThreadedBinaryTree(sample)
            self.assertEqual(sorted(sample), self.inorder(tree))

            sample_size = random.randint(1, len(characters))
            sample = random.sample(characters, sample_size)

            tree = ThreadedBinaryTree(sample)
            self.assertEqual(sorted(sample), self.inorder(tree))

        # Try insertion with duplicates
        sample_size = random.randint(1, self.max_sample_size)
        random_sample = random.sample(numbers, sample_size)
        for _ in range(1, random.randint(2, 10)):
            random_sample.append(random.choice(random_sample))
        with self.assertWarns(DuplicateNodeWarning):
            tree = ThreadedBinaryTree(random_sample)
            self.assertEqual(sorted(set(random_sample)), self.inorder(tree))

    def traversal_testing(self, tree: ThreadedBinaryTree, items):
        self.assertEqual(items, self.level_wise_items(tree))
        self.assertEqual(items, tree.array_repr)
        self.assertEqual(sorted(items), tree.inorder())

    @staticmethod
    def inorder(tree: ThreadedBinaryTree):
        def insert_inorder(node: Optional[ThreadedNode]) -> None:
            if node:
                insert_inorder(node.left if node.left_is_child else None)
                array.append(node.data)
                insert_inorder(node.right if node.right_is_child else None)

        if not tree:
            return
        array: list[Any] = []
        insert_inorder(tree.root)
        return array

    @staticmethod
    def level_wise_items(tree) -> list[Any]:
        result: list[Any] = []
        if not tree:
            return result
        queue: Queue = Queue()
        if tree.root:
            queue.enqueue(tree.root)
        while not queue.is_empty():
            node: ThreadedNode = queue.dequeue()
            result.append(node.data)
            if node.left_is_child:
                queue.enqueue(node.left)
            if node.right_is_child:
                queue.enqueue(node.right)
        return result


if __name__ == '__main__':
    unittest.main()
