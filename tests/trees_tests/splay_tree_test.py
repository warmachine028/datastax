from __future__ import annotations

import random
import unittest

from datastax.errors import (
    NodeNotFoundWarning,
    DeletionFromEmptyTreeWarning,
    DuplicateNodeWarning
)
from datastax.trees import SplayTree
from tests.trees_tests.common_helper_functions import (
    inorder_items, level_wise_items, check_bst_property
)


class TestSplayTree(unittest.TestCase):
    def setUp(self) -> None:
        self.s_tree = SplayTree()
        self.test_cases = 100
        self.max_sample_size = 10

    def test_array_representation(self):
        testcases = [
            [*range(10)],
            [None, 10],
            [10, None, None],
            ['root', None, None, 'child']
        ]
        results = [
            [*range(9, -1, -1)],
            [],
            [10],
            ['child', 'root']
        ]
        for testcase, result in zip(testcases, results):
            tree = SplayTree(testcase)
            self.assertEqual(result, tree.array_repr)

    def test_construction(self):
        numbers = range(1, 1000)
        for _ in range(self.test_cases):
            sample_size = random.randint(1, self.max_sample_size)
            sample = random.sample(numbers, sample_size)

            tree = SplayTree(sample)
            self.assertEqual(sorted(sample), inorder_items(tree))
            # Check deletion after insertion
            to_delete = sample[random.randint(0, len(sample)) - 1]
            tree.delete(to_delete)
            check_bst_property(tree.root)
            # Test insertion after deletion
            tree.insert(to_delete)
            check_bst_property(tree.root)
            self.assertEqual(to_delete, tree.root.data)

    def test_delete(self):
        # Test deletion from empty Tree
        with self.assertWarns(DeletionFromEmptyTreeWarning):
            tree = SplayTree()
            tree.delete()
            self.assertEqual([], level_wise_items(tree))

        sample = random.sample(range(100), self.max_sample_size)
        tree = SplayTree(sample)

        # Attempting deletion of invalid item from empty tree
        with self.assertWarns(NodeNotFoundWarning):
            tree.delete(404)
        # The largest node is slayed
        self.assertEqual(max(sample), tree.root.data)

        temp = list(sample)
        for item in sample:
            tree.delete(item)
            temp.remove(item)
            self.assertEqual(sorted(temp), inorder_items(tree))
        # checking Emptiness
        self.assertTrue([] == tree.array_repr == level_wise_items(tree))
        # Attempting deletion from empty tree
        with self.assertWarns(DeletionFromEmptyTreeWarning):
            tree.delete(404)

        # Attempt insertion after deletion
        insertion_order = random.sample(range(10), self.max_sample_size)
        for i, item in enumerate(insertion_order):
            tree.insert(item)
            self.assertEqual(item, tree.root.data)
            self.assertEqual(sorted(insertion_order[:i + 1]),
                             inorder_items(tree))
            if not i:
                self.assertEqual(item, tree.root.data)

    def test_insertion(self):
        numbers = range(1, 10000)
        for _ in range(self.test_cases):
            tree = self.s_tree
            sample_size = random.randint(1, self.max_sample_size)
            sample = random.sample(numbers, sample_size)
            for item in sample:
                tree.insert(item)

            # Check deletion after insertion
            to_delete = random.choice(sample)
            tree.delete(to_delete)
            temp = list(sample)
            temp.remove(to_delete)
            self.assertEqual(sorted(temp), inorder_items(tree))
            # Again perform insertion
            tree.insert(to_delete)
            self.assertEqual(sorted(sample), inorder_items(tree))
            self.assertTrue(check_bst_property(tree.root))
            # Resetting the tree
            tree._root = None

    def test_insertion_duplicate(self):
        # Test duplicate node insertion: must splay last accessed node
        numbers = range(1, 1000)
        sample_size = random.randint(1, self.max_sample_size)
        sample = random.sample(numbers, sample_size)
        duplicate = random.choice(sample)
        tree = SplayTree(sample)
        with self.assertWarns(DuplicateNodeWarning):
            tree.insert(duplicate)
            self.assertEqual(sorted(sample), inorder_items(tree))
        self.assertEqual(duplicate, tree.root.data)

    def test_search_empty_tree(self):
        with self.assertWarns(NodeNotFoundWarning):
            self.s_tree.search(404)

        # Filling the tree
        sample = random.sample(range(1, 100), 5)
        for item in sample:
            self.s_tree.insert(item)

        # Emptying the tree
        for item in sample:
            self.s_tree.delete(item)

        # Then performing search
        with self.assertWarns(NodeNotFoundWarning):
            self.s_tree.search(404)

    def test_search_invalid_item(self):
        # Filling the tree
        sample = random.sample(range(1, 100), 5)
        for item in sample:
            self.s_tree.insert(item)

        with self.assertWarns(NodeNotFoundWarning):
            self.s_tree.search(404)
            self.assertEqual(max(sample), self.s_tree.root.data)
            self.s_tree.search(-1)
            self.assertEqual(min(sample), self.s_tree.root.data)

    def test_deletion_empty_tree(self):
        with self.assertWarns(DeletionFromEmptyTreeWarning):
            self.s_tree.delete(404)

        # Filling the tree
        sample = random.sample(range(1, 100), 5)
        for item in sample:
            self.s_tree.insert(item)

        # Emptying the tree
        for item in sample:
            self.s_tree.delete(item)

        with self.assertWarns(NodeNotFoundWarning):
            self.s_tree.search(404)

        # perform insertion after that
        item = random.choice(sample)
        self.s_tree.insert(item)
        self.assertEqual(item, self.s_tree.root.data)

    def test_deletion_of_root(self):
        for _ in range(self.test_cases):
            # Filling the tree
            sample = random.sample(range(1, 100), 5)
            for item in sample:
                self.s_tree.insert(item)

            # Emptying the tree
            for _ in sample:
                self.s_tree.delete(self.s_tree.root.data)

            # Tree must be empty
            self.assertEqual(None, self.s_tree.root)
            self.assertEqual([], level_wise_items(self.s_tree))

            # perform insertion after that
            item = random.choice(sample)
            self.s_tree.insert(item)
            self.assertEqual(item, self.s_tree.root.data)
            self.s_tree._root = None

    def test_delete_invalid_item(self):
        for _ in range(self.test_cases):
            # Filling the tree
            sample = random.sample(range(1, 100), 5)
            for item in sample:
                self.s_tree.insert(item)
            with self.assertWarns(NodeNotFoundWarning):
                self.s_tree.delete(404)
                self.assertEqual(max(sample), self.s_tree.root.data)

                self.s_tree.delete(-1)
                self.assertEqual(min(sample), self.s_tree.root.data)

            self.assertEqual(sorted(sample), inorder_items(self.s_tree))
            self.assertTrue(check_bst_property(self.s_tree.root))
            # resetting the tree
            self.s_tree._root = None

    def test_search(self):
        sample = random.sample(range(10), 10)
        item = random.choice(sample)
        tree = SplayTree(sample)
        self.assertEqual(item, tree.search(item).data)
        with self.assertWarns(NodeNotFoundWarning):
            self.assertNotEqual(11, tree.search(11).data)
        self.assertTrue(bool(tree.search(random.choice(sample))))
        self.assertEqual(sorted(sample), inorder_items(tree))
        self.assertTrue(check_bst_property(tree.root))


if __name__ == '__main__':
    unittest.main()
