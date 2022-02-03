import random
import string
import unittest

from datastax.errors import (
    PathNotGivenError,
    PathNotFoundError,
    PathAlreadyOccupiedWarning,
    DeletionFromEmptyTreeWarning,
    NodeNotFoundWarning
)
from datastax.trees import BinaryTree, TreeNode
from tests.trees_tests.common_helper_functions import level_wise_items


class TestBinaryTree(unittest.TestCase):

    def setUp(self) -> None:
        self.bt = BinaryTree()
        self.test_cases = 10
        self.max_sample_size = 10
        self.print_test_cases = [
            [1],
            [None, 10],
            [10, None, None],
            ['root', None, None, 'child'],
            ["1", "B", "Baxy", "D"],
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
            ['root']
        ]
        for testcase, result in zip(testcases, results):
            tree = BinaryTree(testcase)
            self.assertEqual(result, tree.array_repr)

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
            tree = BinaryTree(item)
            # checking tree items
            self.assertEqual(result[0], level_wise_items(tree))
            # checking root
            self.assertEqual(result[1], tree.root.data if tree.root else None)

        # Construct with existing root
        root_node = TreeNode(10)
        tree = BinaryTree([*range(9, 0, -1)], root_node)
        self.assertEqual([*range(10, 0, -1)], level_wise_items(tree))

    def test_delete(self):
        # Test deletion from empty Tree
        with self.assertWarns(DeletionFromEmptyTreeWarning):
            tree = BinaryTree()
            self.assertEqual(tree.delete(), None)
            self.assertEqual([], level_wise_items(tree))

        sample = random.sample(range(100), self.max_sample_size)
        tree = BinaryTree(sample)
        random.shuffle(sample)
        # Attempting deletion of invalid item from empty tree
        with self.assertWarns(NodeNotFoundWarning):
            tree.delete(404)
        for i in sample:
            self.assertEqual(i, tree.delete(i))
        # checking Emptiness
        self.assertTrue([] == tree.array_repr == level_wise_items(tree))
        # Attempting deletion from empty tree
        with self.assertWarns(DeletionFromEmptyTreeWarning):
            tree.delete(404)

        tree.insert(10)
        self.assertEqual(10, tree.root.data)
        self.assertEqual([10], level_wise_items(tree))

    def test_delete_deepest(self):
        # Test deletion from empty Tree
        with self.assertWarns(DeletionFromEmptyTreeWarning):
            tree = BinaryTree()
            self.assertEqual(tree.delete_deepest(), None)
            self.assertEqual([], level_wise_items(tree))

        # Test deletion with only Root
        tree = BinaryTree([1])
        self.assertEqual(tree.delete_deepest(), 1)
        self.assertEqual([], level_wise_items(tree))

        # Test deletion with root and both children
        tree = BinaryTree([1, 2, 3])
        self.assertEqual(tree.delete_deepest(), 3)
        self.assertEqual([1, 2], level_wise_items(tree))

        # Test deletion with root and left child only
        tree = BinaryTree([1, 2])
        self.assertEqual(tree.delete_deepest(), 2)
        self.assertEqual([1], level_wise_items(tree))

        # Test deletion with root and right child only
        tree = BinaryTree([1, None, 3])
        self.assertEqual(tree.delete_deepest(), 3)
        self.assertEqual([1], level_wise_items(tree))

        # Test deletion from a perfect BinaryTree
        tree = BinaryTree([*range(2 ** 3 - 1)])
        self.assertEqual(tree.delete_deepest(), 2 ** 3 - 2)
        self.assertEqual([*range(2 ** 3 - 2)], level_wise_items(tree))

    def test_insert(self):
        tree = BinaryTree([10, None, 20, None, 50])
        tree.insert(None)
        self.assertEqual([10, 20, 50], level_wise_items(tree))
        tree.insert(10)
        tree.insert(20)
        tree.insert(50)
        self.assertEqual([10, 10, 20, 20, 50, 50], level_wise_items(tree))
        tree.insert_path(30, ['left', 'right', 'left'])
        self.assertEqual([10, 10, 20, 20, 50, 50, 30], level_wise_items(tree))

    def test_insert_path(self):
        # inserting root without path
        tree = BinaryTree()
        tree.insert_path(10)
        self.assertEqual([10], level_wise_items(tree))
        # testing inserting
        left, right = "left", "right"
        paths = [
            None,
            [left],
            [right],
            [left, right],
            [left, left],
        ]

        for i in range(1, 6):
            self.bt.insert_path(i, paths[i - 1])
        self.assertEqual([1, 2, 3, 5, 4], level_wise_items(self.bt))

        # Unsuccessful insertion Must require path for non root nodes
        with self.assertRaises(PathNotGivenError):
            self.bt.insert_path(10, None)

        with self.assertRaises(PathNotFoundError):
            self.bt.insert_path(10, [left, left, left, right])

        # Must Warn the user
        with self.assertWarns(PathAlreadyOccupiedWarning):
            self.bt.insert_path(10, [left, left])

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
            BinaryTree([1, 2]).root,  # -> Node
            BinaryTree([1, 2]),  # ->  self referential type
            None  # -> * can't be inserted anywhere
            # entire list will be discarded if Node as first element
        ]

        tree = BinaryTree(items)

        self.assertEqual(items[:-1], level_wise_items(tree))

    def test_preorder_print(self):

        results = [
            '\n1', 'NULL', '\n10', '\nroot',
            '\n1'
            '\n├─▶ B'  # Normal BinaryTree Repr
            '\n│   └─▶ D'
            '\n└─▶ Baxy',

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
            '\n    └─▶ 3'  # An example of a degenerate tree
            '\n        └─▶ 4'
            '\n            └─▶ 5'

        ]

        for testcase, result in zip(self.print_test_cases, results):
            tree = BinaryTree(testcase)
            tree.preorder_print()
            self.assertEqual(result, tree._string)

    def test_string_representation(self):
        results = [
            '   1  \n', '  NULL', '  10  \n', '  root  \n',
            '                1               \n'
            '        ┌───────┴───────┐       \n'
            '        B             Baxy      \n'  # Normal BinaryTree Repr
            '    ┌───┘                       \n'
            '    D                           \n',

            '                    4                   \n'
            '          ┌─────────┴─────────┐         \n'
            '          4                   4         \n'
            '     ┌────┴────┐         ┌────┘         \n'
            '     4         3       [\'1\']            \n',

            '        (10, 20)        \n'
            '      ┌─────┘           \n'
            '  [10, 20]              \n',

            f"{' ' * 48}1                        {' ' * 23}\n"
            f"{' ' * 48}└───────────────────────┐{' ' * 23}\n"
            f"{' ' * 48}                        2{' ' * 23}\n"
            f"{' ' * 48}            ┌───────────┘{' ' * 23}\n"  # An example of
            f"{' ' * 48}            3            {' ' * 23}\n"  # Degenerate
            f"{' ' * 48}            └─────┐      {' ' * 23}\n"  # Tree
            f"{' ' * 48}                  4      {' ' * 23}\n"
            f"{' ' * 48}               ┌──┘      {' ' * 23}\n"
            f"{' ' * 48}               5         {' ' * 23}\n"
        ]

        for testcase, result in zip(self.print_test_cases, results):
            tree = BinaryTree(testcase)
            self.assertEqual(result, tree.__str__())

    def test_with_random_inputs(self):
        numbers = range(-100, 100)
        characters = string.ascii_uppercase + string.ascii_lowercase
        for _ in range(self.test_cases):
            sample_size = random.randint(1, self.max_sample_size)
            sample = random.sample(numbers, sample_size)

            # Constructing tree with random numbers
            tree = BinaryTree(sample)
            self.assertEqual(sample, level_wise_items(tree))

            sample_size = random.randint(1, len(characters))
            sample = random.sample(characters, sample_size)

            # Constructing tree with random character set
            tree = BinaryTree(sample)
            self.assertEqual(sample, level_wise_items(tree))


if __name__ == '__main__':
    unittest.main()
