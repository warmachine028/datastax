import unittest

from datastax.trees import HuffmanTree


class TestHuffmanTree(unittest.TestCase):
    def setUp(self) -> None:
        self.hufT = HuffmanTree()

    def test1(self):
        tree = HuffmanTree("ABBCDBCCDAABBEEEBEAB")

        print(tree)

        tree = HuffmanTree("Espresso express")
        print(tree)
