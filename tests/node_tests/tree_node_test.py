import io
import sys
import unittest
from datastax.Nodes import TreeNode


class TestTreeNode(unittest.TestCase):
    def test_string(self):
        expected = "       10       \n"
        self.assertEqual(str(TreeNode(10)), expected)

        expected = \
            "10\n" \
            "\n"

        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            TreeNode(10).preorder_print()
            sys.stdout = sys.__stdout__
            self.assertEqual(expected, captured_output.getvalue())

    def test_with_left_child(self):
        left_child = TreeNode(20)
        node = TreeNode(10, left=left_child)
        expected = \
            "       10       \n" \
            "    ┌───┘\n" \
            "   20   "
        self.assertEqual(expected, str(node))

        expected = \
            "10\n" \
            "└─▶ 20\n"

        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            node.preorder_print()
            sys.stdout = sys.__stdout__
            self.assertEqual(expected, captured_output.getvalue())

    def test_with_right_child(self):
        right_child = TreeNode(39)
        node = TreeNode(10, right=right_child)
        expected = \
            "       10       \n" \
            "        └───┐\n" \
            "           39   "
        self.assertEqual(expected, str(node))

        expected = \
            "10\n" \
            "└─▶ 39\n"

        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            node.preorder_print()
            sys.stdout = sys.__stdout__
            self.assertEqual(expected, captured_output.getvalue())

    def test_with_left_and_right_children(self):
        left_child = TreeNode(30)
        right_child = TreeNode(39)
        node = TreeNode(10, left=left_child, right=right_child)
        expected = \
            "     10     \n" \
            "   ┌──┴──┐\n" \
            "  30    39  "
        self.assertEqual(expected, str(node))

        expected = \
            '10\n' \
            '├─▶ 30\n' \
            '└─▶ 39\n'

        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            node.preorder_print()
            sys.stdout = sys.__stdout__
            self.assertEqual(expected, captured_output.getvalue())

    def test_with_left_as_None(self):
        node = TreeNode(10, TreeNode(None))
        expected = \
            '       10       \n' \
            '    ┌───┘\n' \
            '  None  '
        self.assertEqual(expected, str(node))

        expected = \
            '10\n' \
            '└─▶ None\n'

        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            node.preorder_print()
            sys.stdout = sys.__stdout__
            self.assertEqual(expected, captured_output.getvalue())

    def test_with_right_as_None(self):
        node = TreeNode(10, None, TreeNode(None))
        result = \
            '       10       \n' \
            '        └───┐\n' \
            '          None  '
        self.assertEqual(result, str(node))

        expected = \
            '10\n' \
            '└─▶ None\n'

        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            node.preorder_print()
            sys.stdout = sys.__stdout__
            self.assertEqual(expected, captured_output.getvalue())

    def test_with_both_as_None(self):
        node = TreeNode(10, TreeNode(None), TreeNode(None))
        expected = \
            '       10       \n' \
            '    ┌───┴───┐\n' \
            '  None    None  '
        self.assertEqual(expected, str(node))

        expected = \
            '10\n' \
            '├─▶ None\n' \
            '└─▶ None\n'

        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            node.preorder_print()
            sys.stdout = sys.__stdout__
            self.assertEqual(expected, captured_output.getvalue())

    def test_with_left_child_as_None(self):
        node = TreeNode(10, None)
        expected = \
            '       10       \n'

        self.assertEqual(expected, str(node))

        expected = \
            '10\n' \
            '\n'

        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            node.preorder_print()
            sys.stdout = sys.__stdout__
            self.assertEqual(expected, captured_output.getvalue())

    def test_with_right_child_as_None(self):
        node = TreeNode(10, TreeNode(10), None)
        result = \
            '       10       \n' \
            '    ┌───┘\n' \
            '   10   '

        self.assertEqual(result, str(node))

        expected = \
            '10\n' \
            '└─▶ 10\n'

        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            node.preorder_print()
            sys.stdout = sys.__stdout__
            self.assertEqual(expected, captured_output.getvalue())

    def test_with_both_child_as_None(self):
        node = TreeNode(10, None, None)
        result = \
            '       10       \n'

        self.assertEqual(result, str(node))

        expected = \
            '10\n' \
            '\n'

        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            node.preorder_print()
            sys.stdout = sys.__stdout__
            self.assertEqual(expected, captured_output.getvalue())

    def test_with_data_as_None(self):
        node = TreeNode(None, )
        result = \
            '      None      \n'

        self.assertEqual(result, str(node))

        expected = \
            'None\n' \
            '\n'

        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            node.preorder_print()
            sys.stdout = sys.__stdout__
            self.assertEqual(expected, captured_output.getvalue())

    def test_with_data_as_0(self):
        node = TreeNode(0, None, None)
        result = '        0       \n'

        self.assertEqual(result, str(node))

        expected = \
            '0\n' \
            '\n'

        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            node.preorder_print()
            sys.stdout = sys.__stdout__
            self.assertEqual(expected, captured_output.getvalue())

    def test_with_data_set_left(self):
        node = TreeNode(10)
        left = TreeNode(20)
        node.set_left(left)

        self.assertEqual(left, node.left)
        self.assertEqual(None, node.right)
        self.assertEqual(20, node.left.data)

    def test_with_data_set_right(self):
        node = TreeNode(10)
        right = TreeNode(20)
        node.set_right(right)

        self.assertEqual(right, node.right)
        self.assertEqual(None, node.left)
        self.assertEqual(20, node.right.data)


if __name__ == '__main__':
    unittest.main()
