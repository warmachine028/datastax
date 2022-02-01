from __future__ import annotations

import unittest

from datastax.trees import SplayTree


class TestSplayTree(unittest.TestCase):
    def setUp(self) -> None:
        self.s_tree = SplayTree()

    def test(self):
        tree = SplayTree([1, 2, 3, 4])
        tree.search(1)
        tree.insert(10)
        tree.delete(10)
        print(tree)


if __name__ == '__main__':
    unittest.main()
