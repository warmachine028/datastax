import random
import string
import unittest

from datastax.errors import (
    DuplicateNodeWarning,
    NodeNotFoundWarning,
    DeletionFromEmptyTree
)
from datastax.trees import AVLTree, AVLNode
from tests.trees_tests.common_helper_functions import (
    level_wise_items,
    inorder_items
)


class TestAVLTree(unittest.TestCase):

    def setUp(self) -> None:
        self.avt = AVLTree()
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
            [3, 1, 7, 0, 2, 5, 8, 4, 6, 9],
            [],
            [10],
            ['root', 'child']
        ]
        for testcase, result in zip(testcases, results):
            tree = AVLTree(testcase)
            self.assertEqual(result, tree.array_repr)

    def test_balance_factor(self):
        numbers = range(-100, 100)
        for _ in range(self.test_cases):
            sample_size = random.randint(1, self.max_sample_size)
            sample = random.sample(numbers, sample_size)

            # Constructing tree with random numbers
            tree = AVLTree(sample)
            self.assertTrue(-1 <= tree.balance_factor() <= 1)

    def test_construction(self):
        items = [
            [*range(1, 7)],  # <- Using general list of ints
            [*range(10)],  # <- Using range object unpacking in list
            [],  # <- Using Empty list
            [None],  # <- Using only None item passed through list
            [None, 1, 2, 3, 4, 5],  # <- Using First item as None
            None,  # <- Using None passed directly
        ]
        results = [
            [[4, 2, 5, 1, 3, 6], 4],
            [[3, 1, 7, 0, 2, 5, 8, 4, 6, 9], 3],
            [[], None],
            [[], None],
            [[], None],
            [[], None]
        ]
        for item, result in zip(items, results):
            tree = AVLTree(item)
            # checking tree items
            self.assertEqual(result[0], level_wise_items(tree))
            # checking root
            self.assertEqual(result[1], tree.root.data if tree.root else None)

        # Construct with existing root
        root_node = AVLNode(6)
        with self.assertWarns(DuplicateNodeWarning):
            tree = AVLTree([*range(9, 0, -1)], root_node)
            self.assertEqual([6, 4, 8, 2, 5, 7, 9, 1, 3],
                             level_wise_items(tree))

    def test_delete(self):
        # Test deletion from empty Tree
        with self.assertWarns(DeletionFromEmptyTree):
            tree = AVLTree()
            self.assertEqual(tree.delete(), None)
            self.assertEqual([], level_wise_items(tree))

        sample = random.sample(range(100), self.max_sample_size)
        tree = AVLTree(sample)

        # Attempting deletion of invalid item from empty tree
        with self.assertWarns(NodeNotFoundWarning):
            tree.delete(404)

        temp = list(sample)
        for item in sample:
            tree.delete(item)
            temp.remove(item)
            self.assertTrue(-1 <= tree.balance_factor() <= 1)
            self.assertEqual(sorted(temp), inorder_items(tree))
        # checking Emptiness
        self.assertTrue([] == tree.array_repr == level_wise_items(tree))
        # Attempting deletion from empty tree
        with self.assertWarns(DeletionFromEmptyTree):
            tree.delete(404)

        # Attempt insertion after deletion
        insertion_order = random.sample(range(10), self.max_sample_size)
        for i, item in enumerate(insertion_order):
            tree.insert(item)
            self.assertTrue(-1 <= tree.balance_factor() <= 1)
            self.assertEqual(sorted(insertion_order[:i + 1]),
                             inorder_items(tree))

            if not i:
                self.assertEqual(item, tree.root.data)

    def test_height(self):
        tree = AVLTree([4, 3, 1, 5, 2, 9])
        # Height of root with both nodes
        self.assertEqual(3, tree.height(AVLTree([3, 1, 2, 5]).root))
        self.assertEqual(2, tree.height(tree.root.left))
        self.assertEqual(2, tree.height(tree.root.right))
        self.assertEqual(1, tree.height(tree.root.left.right))
        self.assertEqual(0, tree.height(tree.root.left.left))
        self.assertEqual(0, tree.height(AVLTree().root))

    def test_insert(self):
        self.assertEqual([], level_wise_items(self.avt))

        # testing insertion
        data = [4, 3, 1, 2, 5, 3, 2, 1, 9]
        results = [
            [4],
            [4, 3],
            [3, 1, 4],
            [3, 1, 4, 2],
            [3, 1, 4, 2, 5],
            [3, 1, 5, 2, 4, 9]
        ]
        # Normal inserting
        for item, result in zip(data[:5], results[:5]):
            self.avt.insert(item)
            self.assertTrue(-1 <= self.avt.balance_factor() <= 1)
            self.assertEqual(result, level_wise_items(self.avt))

        # Testing warnings
        for item in data[5:-1]:
            with self.assertWarns(DuplicateNodeWarning):
                self.avt.insert(item)

        self.avt.insert(data[-1])
        self.assertEqual(results[-1], level_wise_items(self.avt))
        self.assertTrue(-1 <= self.avt.balance_factor() <= 1)

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
            AVLTree([1, 2]).root,  # -> Node
            AVLTree([1, 2]),  # ->  self referential type
            None  # -> * can't be inserted anywhere
            # entire list will be discarded if Node as first element
        ]  # Can't even insert the rest of the items

        # Can't perform comparison operation between heterogeneous items
        with self.assertRaises(TypeError):
            AVLTree(items)

    def test_preorder_print(self):
        results = [
            '\n1', 'NULL', '\n10', '\nroot'
                                   '\n└─▶ child',

            '\nB'
            '\n├─▶ 1'
            '\n└─▶ Baxy'  # Normal AVLTree Repr
            '\n    └─▶ D',

            '\n2'
            '\n├─▶ 1'
            '\n└─▶ 4'  # An example of a perfectly balanced binary tree
            '\n    ├─▶ 3'
            '\n    └─▶ 5'
        ]

        for testcase, result in zip(self.print_test_cases, results):
            tree = AVLTree(testcase)
            tree.preorder_print()
            self.assertEqual(result, tree._string)

    def test_search(self):
        sample = random.sample(range(10), 10)
        item = random.choice(sample)
        tree = AVLTree(sample)
        self.assertEqual(item, tree.search(item).data)
        self.assertEqual(None, tree.search(11))
        items = [3, 1, 0, 6, 4, 7, 8, 9, 2, 5]
        tree = AVLTree(items)
        self.assertEqual(True, bool(tree.search(1)))
        self.assertEqual(True, bool(tree.search(9)))

    def test_string_representation(self):
        results = [
            '   1  \n', '  NULL', '  10  \n',
            '        root        \n'
            '     ┌────┘         \n'
            '   child            \n',

            '                B               \n'
            '        ┌───────┴───────┐       \n'
            '        1             Baxy      \n'  # Normal AVLTree Repr
            '                        └───┐   \n'
            '                            D   \n',

            # An example of a perfectly balanced binary Tree
            '            2           \n'
            '      ┌─────┴─────┐     \n'
            '      1           4     \n'
            '               ┌──┴──┐  \n'
            '               3     5  \n'
        ]

        for testcase, result in zip(self.print_test_cases, results):
            tree = AVLTree(testcase)
            self.assertEqual(result, tree.__str__())

    def test_with_random_inputs(self):
        numbers = range(-100, 100)
        characters = string.ascii_uppercase + string.ascii_lowercase
        # To avoid terminal explosion please avoid printing these trees
        # after construction
        for _ in range(self.test_cases):
            sample_size = random.randint(1, self.max_sample_size)
            sample = random.sample(numbers, sample_size)

            # Constructing tree with random numbers
            tree = AVLTree(sample)
            self.assertTrue(-1 <= tree.balance_factor() <= 1)
            self.assertEqual(sorted(sample), inorder_items(tree))

            sample_size = random.randint(1, len(characters))
            sample = random.sample(characters, sample_size)

            # Constructing tree with random character set
            tree = AVLTree(sample)
            self.assertTrue(-1 <= tree.balance_factor() <= 1)
            self.assertEqual(sorted(sample), inorder_items(tree))

        # Try insertion with duplicates
        sample_size = random.randint(1, self.max_sample_size)
        random_sample = random.sample(numbers, sample_size)
        for _ in range(1, random.randint(2, 10)):
            random_sample.append(random.choice(random_sample))
        with self.assertWarns(DuplicateNodeWarning):
            tree = AVLTree(random_sample)
            self.assertEqual(sorted(set(random_sample)),
                             inorder_items(tree))

    if __name__ == '__main__':
        unittest.main()
