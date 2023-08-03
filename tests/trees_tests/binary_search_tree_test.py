import random
import string
import unittest
from datastax.Utils.Warnings import (
    DuplicateNodeWarning,
    DeletionFromEmptyTreeWarning,
    NodeNotFoundWarning
)
from datastax.Trees import BinarySearchTree
from datastax.Nodes import TreeNode
from tests.trees_tests.common_helper_functions import (
    level_wise_items,
    inorder_items,
    check_bst_property
)


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self) -> None:
        self.bst = BinarySearchTree()
        self.test_cases = 10
        self.max_sample_size = 10
        self.print_test_cases = [
            [1],
            [None, 10],
            [10, None, None],
            ['root', None, None, 'child'],
            ["1", "B", "Baxy", "D"],
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
            tree = BinarySearchTree(testcase)
            self.assertEqual(result, tree.array_repr)

    def test_construction(self):
        items = [
            [1, 2, 3, 4, 5, 6],  # <- Using general list of ints
            [*range(10)],  # <- Using range object unpacking in list
            [],  # <- Using Empty list
            [None],  # <- Using only None item passed through list
            [None, *range(1, 6)],  # <- Using First item as None
            None,  # <- Using None passed directly
        ]
        results = [
            [[*range(1, 7)], 1],
            [[*range(10)], 0],
            [[], None],
            [[], None],
            [[], None],
            [[], None]
        ]

        for item, result in zip(items, results):
            tree = BinarySearchTree(item)
            # checking tree items
            self.assertEqual(result[0], level_wise_items(tree))
            # checking root
            self.assertEqual(result[1], tree.root.data if tree.root else None)
            # check bst property
            self.assertTrue(check_bst_property(tree.root))

        # Construct with existing root
        root_node = TreeNode(6)
        with self.assertWarns(DuplicateNodeWarning):
            tree = BinarySearchTree([*range(9, 0, -1)], root=root_node)
            self.assertEqual([6, 5, 9, 4, 8, 3, 7, 2, 1],
                             level_wise_items(tree))

    def test_delete(self):
        # Test deletion from empty Tree
        with self.assertWarns(DeletionFromEmptyTreeWarning):
            tree = BinarySearchTree()
            self.assertEqual(tree.delete(), None)
            self.assertEqual([], level_wise_items(tree))

        sample = random.sample(range(100), self.max_sample_size)
        tree = BinarySearchTree(sample)
        # Attempting deletion of invalid item from empty tree
        with self.assertWarns(NodeNotFoundWarning):
            tree.delete(404)

        temp = list(sample)
        for item in sample:
            tree.delete(item)
            temp.remove(item)
            self.assertEqual(sorted(temp), inorder_items(tree))
            self.assertTrue(check_bst_property(tree.root))

        # Attempting deletion from empty tree
        with self.assertWarns(DeletionFromEmptyTreeWarning):
            tree.delete(404)

        # Attempt insertion after deletion
        insertion_order = random.sample(range(10), self.max_sample_size)
        for i, item in enumerate(insertion_order):
            tree.insert(item)
            self.assertEqual(sorted(insertion_order[:i + 1]),
                             inorder_items(tree))
            self.assertTrue(check_bst_property(tree.root))

    def test_insert(self):
        self.assertEqual([], level_wise_items(self.bst))

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
            self.bst.insert(item)
            self.assertEqual(result, level_wise_items(self.bst))
            self.assertTrue(check_bst_property(self.bst.root))

        # Testing warnings
        for item in data[5:-1]:
            with self.assertWarns(DuplicateNodeWarning):
                self.bst.insert(item)

        self.bst.insert(data[-1])
        self.assertEqual(results[-1], level_wise_items(self.bst))

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
            BinarySearchTree([1, 2]).root,  # -> Node
            BinarySearchTree([1, 2]),  # ->  self referential type
            None  # -> * can't be inserted anywhere
            # entire list will be discarded if Node as first element
        ]  # Can't even insert the rest of the items

        # Can't perform comparison operation between heterogeneous items
        with self.assertRaises(TypeError):
            BinarySearchTree(items)

    def test_preorder_print(self):
        results = [
            '\n1', 'NULL', '\n10', '\nroot'
                                   '\n└─▶ child',

            '\n1'
            '\n└─▶ B'  # Normal BinarySearchTree Repr
            '\n    └─▶ Baxy'
            '\n        └─▶ D',

            '\n1'
            '\n└─▶ 2'
            '\n    └─▶ 3'  # An example of a right skewed tree
            '\n        └─▶ 4'
            '\n            └─▶ 5'

        ]

        for testcase, result in zip(self.print_test_cases, results):
            tree = BinarySearchTree(testcase)
            tree.preorder_print()
            self.assertEqual(result, tree._string)

    def test_search(self):
        sample = random.sample(range(10), 10)
        item = random.choice(sample)
        tree = BinarySearchTree(sample)
        self.assertEqual(item, tree.search(item).data)
        with self.assertWarns(NodeNotFoundWarning):
            self.assertIsNone(tree.search(11))
        self.assertTrue(bool(tree.search(random.choice(sample))))
        self.assertEqual(sorted(sample), inorder_items(tree))
        self.assertTrue(check_bst_property(tree.root))

    def test_string_representation(self):
        results = [
            '   1  \n', '  NULL', '  10  \n',
            '        root        \n'
            '     ┌────┘         \n'
            '   child            \n',

            f"{' ' * 32}1                               \n"
            f"{' ' * 32}└───────────────┐               \n"  # Normal
            f"{' ' * 32}                B               \n"  # BinarySearchTree
            f"{' ' * 32}                └───────┐       \n"  # Repr
            f"{' ' * 32}                      Baxy      \n"
            f"{' ' * 32}                        └───┐   \n"
            f"{' ' * 32}                            D   \n",

            # An example of a right skewed binary Tree
            f"{' ' * 48}1                                               \n"
            f"{' ' * 48}└───────────────────────┐                       \n"
            f"{' ' * 48}                        2                       \n"
            f"{' ' * 48}                        └───────────┐           \n"
            f"{' ' * 48}                                    3           \n"
            f"{' ' * 48}                                    └─────┐     \n"
            f"{' ' * 48}                                          4     \n"
            f"{' ' * 48}                                          └──┐  \n"
            f"{' ' * 48}                                             5  \n",
        ]

        for testcase, result in zip(self.print_test_cases, results):
            tree = BinarySearchTree(testcase)
            self.assertEqual(result, tree.__str__())

    def test_with_random_inputs(self):
        numbers = range(-100, 100)
        characters = string.ascii_uppercase + string.ascii_lowercase
        # To avoid terminal explosion please avoid printing these Trees
        # after construction
        for _ in range(self.test_cases):
            sample_size = random.randint(1, self.max_sample_size)
            sample = random.sample(numbers, sample_size)

            # Constructing tree with random numbers
            tree = BinarySearchTree(sample)
            self.assertEqual(sorted(sample), inorder_items(tree))
            self.assertTrue(check_bst_property(tree.root))

            sample_size = random.randint(1, len(characters))
            sample = random.sample(characters, sample_size)

            # Constructing tree with random characters
            tree = BinarySearchTree(sample)
            self.assertEqual(sorted(sample), inorder_items(tree))
            self.assertTrue(check_bst_property(tree.root))

        # Try insertion with duplicates
        sample_size = random.randint(1, self.max_sample_size)
        random_sample = random.sample(numbers, sample_size)
        for _ in range(1, random.randint(2, 10)):
            random_sample.append(random.choice(random_sample))
        with self.assertWarns(DuplicateNodeWarning):
            tree = BinarySearchTree(random_sample)
            self.assertEqual(sorted(set(random_sample)), inorder_items(tree))


if __name__ == '__main__':
    unittest.main()
