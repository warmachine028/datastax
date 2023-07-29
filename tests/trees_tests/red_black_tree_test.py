from __future__ import annotations

import random
import unittest

from datastax.errors import (
    NodeNotFoundWarning,
    DeletionFromEmptyTreeWarning
)
from datastax.Trees import RedBlackTree, RedBlackNode
from datastax.Trees.red_black_tree import RED, BLACK
from tests.trees_tests.common_helper_functions import (
    inorder_items, level_wise_items, check_bst_property
)


class TestRedBlackTree(unittest.TestCase):
    def setUp(self) -> None:
        self.rb_tree = RedBlackTree()
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
            [3, 1, 5, 0, 2, 4, 7, 6, 8, 9],
            [],
            [10],
            ['root', 'child']
        ]
        for testcase, result in zip(testcases, results):
            tree = RedBlackTree(testcase)
            self.assertEqual(result, tree.array_repr)

    def test_construction(self):
        numbers = range(1, 10000)
        for _ in range(self.test_cases):
            sample_size = random.randint(1, self.max_sample_size)
            sample = random.sample(numbers, sample_size)

            tree = RedBlackTree(sample)
            self.assertEqual(sorted(sample), inorder_items(tree))
            # Validate Red Black Tree tree
            self.assertTrue(self.validate_tree(tree))
            # Check deletion after insertion
            to_delete = sample[random.randint(0, len(sample)) - 1]
            tree.delete(to_delete)
            self.assertTrue(self.validate_tree(tree))
            tree.insert(to_delete)
            self.assertTrue(self.validate_tree(tree))

    def test_delete(self):
        # Test deletion from empty Tree
        with self.assertWarns(DeletionFromEmptyTreeWarning):
            tree = RedBlackTree()
            tree.delete()
            self.assertEqual([], level_wise_items(tree))

        sample = random.sample(range(100), self.max_sample_size)
        tree = RedBlackTree(sample)

        # Attempting deletion of invalid item from empty tree
        with self.assertWarns(NodeNotFoundWarning):
            tree.delete(404)

        temp = list(sample)
        for item in sample:
            tree.delete(item)
            temp.remove(item)
            self.assertTrue(self.validate_tree(tree))
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
            self.assertTrue(self.validate_tree(tree))
            self.assertEqual(sorted(insertion_order[:i + 1]),
                             inorder_items(tree))

            if not i:
                self.assertEqual(item, tree.root.data)

    def test_insertion(self):
        numbers = range(1, 10000)
        for _ in range(self.test_cases):
            tree = self.rb_tree
            sample_size = random.randint(1, self.max_sample_size)
            sample = random.sample(numbers, sample_size)
            for item in sample:
                tree.insert(item)
            # Validate Red Black Tree tree
            self.assertTrue(self.validate_tree(tree))

            # Check deletion after insertion
            to_delete = sample[random.randint(0, len(sample)) - 1]
            tree.delete(to_delete)
            self.assertTrue(self.validate_tree(tree))
            # Again perform insertion
            tree.insert(to_delete)
            self.assertTrue(self.validate_tree(tree))
            # Resetting the tree
            tree._root = None

    def test_search(self):
        sample = random.sample(range(10), 10)
        item = random.choice(sample)
        tree = RedBlackTree(sample)
        self.assertEqual(item, tree.search(item).data)
        with self.assertWarns(NodeNotFoundWarning):
            self.assertIsNone(tree.search(11))
        self.assertTrue(bool(tree.search(random.choice(sample))))
        self.assertEqual(sorted(sample), inorder_items(tree))
        self.assertTrue(check_bst_property(tree.root))

    def test_with_rogue_rbt(self):
        # Tree with red Red conflict
        root = RedBlackNode(
            500,
            RedBlackNode(400, RedBlackNode(300, None, None, BLACK)),
            RedBlackNode(600, RedBlackNode(550)),
            BLACK
        )
        # creating parental links
        root.left.parent = root.right.parent = root
        root.left.left.parent = root.left
        root.right.left.parent = root.right

        self.assertFalse(self.check_coloring(root))
        self.assertTrue(check_bst_property(root))
        self.assertTrue(self.check_black_height(root))

        # Tree with Red root node
        root = RedBlackNode(
            500,
            RedBlackNode(400, RedBlackNode(300), None, BLACK),
            RedBlackNode(600, RedBlackNode(550), None, BLACK),
        )

        # creating parental links
        root.left.parent = root.right.parent = root
        root.left.left.parent = root.left
        root.right.left.parent = root.right

        self.assertFalse(self.check_coloring(root))
        self.assertTrue(check_bst_property(root))
        self.assertTrue(self.check_black_height(root))

    # All 3 Properties of a Red Black Tree must be valid
    def validate_tree(self, tree: RedBlackTree) -> bool:
        color = self.check_coloring(tree.root)
        bst_property = check_bst_property(tree.root)
        black_height = self.check_black_height(tree.root)
        return color and bst_property and black_height

    # Property 2
    def check_coloring(self, node: RedBlackNode) -> bool:
        """
        :param node: Root of red black Tree
        :return: True if Tree coloring is valid else False
        """
        if not node:  # Reached its Leaf Nodes
            return True
        if node.color not in (RED, BLACK):  # All nodes must be red or black
            return False
        if not node.parent and node.color == RED:  # Root node must be black
            return False
        if node.color == RED:  # Check for Red-Red Conflict
            if node.left and node.left.color == RED:
                return False
            if node.right and node.right.color == RED:
                return False
        # Recursively checking for left and right sub Trees
        left = self.check_coloring(node.left)
        right = self.check_coloring(node.right)
        return left and right

    # Property 3
    @staticmethod
    def check_black_height(node: RedBlackNode) -> bool:
        """
        :param node: Root of red black Tree
        :return: True if black height is valid for all sub Trees else False
        """

        def calculate(root: RedBlackNode) -> int:
            if not root:
                return 1
            if not root.parent:
                return 0
            left_height = calculate(root.left)
            right_height = calculate(root.right)
            _black_height = 1 if root.color is BLACK else 0
            if (
                    left_height != right_height
                    or
                    -1 in (left_height, right_height)
            ):
                return -1
            return left_height + _black_height

        return False if calculate(node) == -1 else True


if __name__ == '__main__':
    unittest.main()
