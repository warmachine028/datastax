import unittest

from datastax.Trees import HuffmanTree


class TestHuffmanTree(unittest.TestCase):
    def setUp(self) -> None:
        self.hufT = HuffmanTree()

    def test1(self):
        tree = HuffmanTree("ABBCDBCCDAABBEEEBEAB")

        print(tree)

        tree = HuffmanTree("Espresso express")
        print(tree)

    def test2(self):
        tree = HuffmanTree("ABBCDBCCDAABBEEEBEAB")
        #
        # print(tree)

        tree = HuffmanTree(
            "A paragraph template is a graphic organizer specifically "
            "designed to assist students in writing a paragraph. In "
            "particular, paragraph templates help students identify the "
            "components of a paragraph (e.g. topic sentence, supporting "
            "details, conclusion) as well as their the sequence and order."
        )
        tree = HuffmanTree("Espresso Espress")
        print(tree)
        print(tree.compression_ratio())
        print(tree.space_saved())
        print(tree.huffman_table)
        Table = tree.huffman_table.data
        Huffman_Code = tree.huffman_code
        tree = HuffmanTree()
        print(tree)
        print(tree.huffman_table)
        print(tree.compression_ratio())
        Message = tree.decode_from_table(Huffman_Code, Table)
        print(Message)

        # print(tree)
        # print(tree.huffman_code)
        # print(tree.huffman_table)
        # print(tree.huffman_table.data)
        # # assert tree.huffman_code_of('E') == '1011'
        # # assert tree.huffman_code_of('s') == '11'
        # # assert tree.huffman_code_of('p') == '011'

    def test3(self):
        h = HuffmanTree()
        c = h.huffman_code_of('A')
        print(c)
