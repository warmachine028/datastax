import unittest

from datastax.errors import (
    UnmatchedBracketPairError,
    InvalidExpressionError
)
from datastax.trees import ExpressionTree
from tests.trees_tests.common_helper_functions import (
    level_wise_items,
    postorder_items
)


class TestExpressionTree(unittest.TestCase):

    def setUp(self) -> None:
        self.expt = ExpressionTree()
        self.test_cases = 10
        self.max_sample_size = 10
        self.print_test_cases = [
            'a',
            [None, 'a', '+', 'b'],
            [1, '+', 2, None],
            ['root', '+', None, None, 'child'],
            [1, '%', ' (', "B", ' + ', "Baxy", ')', '*', "D"],
            ['(', 1, '+', 'b', ')'],
            "D * (6+A)/ C? ",
            'A * B % C / D'
        ]

    def test_array_representation(self):
        testcases = [
            ['a', '+', 'b', '/', 'c', '*', 'd'],
            "(a+(b))",
            [None, 10],
            [10, None, None],
            ['root', '+', None, None, 'child']
        ]

        results = [
            ['+', 'a', '*', '/', 'd', 'b', 'c'],
            ['+', 'a', 'b'],
            [],
            ['10'],
            ['+', 'root', 'child']
        ]

        for testcase, result in zip(testcases, results):
            tree = ExpressionTree(testcase)
            self.assertEqual(result, tree.array_repr)

    def test_construction(self):
        items = [
            # Checking Erroneous Empty Objects first
            [],  # <- Using Empty list
            [None],  # <- Using only None item passed through list
            [None, 1, 2, 3, 4, 5],  # <- Using First item as None
            None,  # <- Using None passed directly

            # Using general list of ints and operators
            [1, '*', 2, '*', 3, '/', 4],
            "a*b/c+e/f*g+k-x*y",  # <- Using infix string with characters
            "1234+99*89/44",  # <- Using infix string with numbers
            "A*(B+C)/D",  # <- Using infix string with chars and brackets
            "a+b*(c^d-e) ^ (f%g*h)-i"  # <- Using ^, %,' ' characters
        ]
        results = [
            [[], None],
            [[], None],
            [[], None],
            [[], None],

            [['/', '*', '4', '*', '3', '1', '2'], '/'],
            [['-', '+', '*', '+', 'k', 'x', 'y', '/',
              '*', '*', 'c', '/', 'g', 'a', 'b', 'e', 'f'], '-'],
            [['+', '1234', '/', '*', '44', '99', '89'], '+'],
            [['/', '*', 'D', 'A', '+', 'B', 'C'], '/'],
            [['-', '+', 'i', 'a', '*', 'b', '^', '-', '*',
              '^', 'e', '%', 'h', 'c', 'd', 'f', 'g'], '-']
        ]
        for item, result in zip(items, results):
            tree = ExpressionTree(item)
            # checking tree items
            self.assertEqual(result[0], level_wise_items(tree))
            # checking root
            self.assertEqual(result[1], tree.root.data if tree.root else None)
            # checking infix and postfix expressions:
            if tree.root:
                self.assertEqual(tree.infix_expression,
                                 ''.join(map(str, item)))
                self.assertEqual(
                    tree.postfix_expression,
                    f"{' '.join(map(str, postorder_items(tree)))} ")

    def test_errors(self):
        # Bracket Missing
        test_cases = [
            "a+b(",
            "a+b)",
            "(a+b",
            "(a+(b)",
            "a*b(c*(d/ e * f)"
        ]
        for test_case in test_cases:
            with self.assertRaises(UnmatchedBracketPairError):
                ExpressionTree(test_case)

        # Bad Expressions
        test_cases = [
            'A + B - * D',
            'A B + C - (9) +-'
        ]
        for test_case in test_cases:
            with self.assertRaises(InvalidExpressionError):
                ExpressionTree(test_case)

    def test_infix_to_postfix(self):
        infix_expressions = [
            "a+    b", "a+(b)", "(a+(b))", "(a)+b",
            "a+b+c", "a*b+c",
            "a+b*(c^d-e)^(f+g*h)-i",
            "A*(B+C)/D",
            ''.join(map(str, [125, '+', 2, '*', 3])),
            "1234+99*89/44",
            "a*b/c+e/f*g+k-x*y"
        ]
        results = [
            *['a b + '] * 4,
            'a b + c + ', 'a b * c + ',
            'a b c d ^ e - f g h * + ^ * + i - ',
            'A B C + * D / ',
            '125 2 3 * + ',
            '1234 99 89 * 44 / + ',
            'a b * c / e f / g * + k + x y * - '
        ]

        for infix_expression, postfix_expression in zip(infix_expressions,
                                                        results):
            converted = ExpressionTree().infix_to_postfix(infix_expression)
            self.assertEqual(postfix_expression, converted)

    def test_insert_path(self):
        # inserting using insert_path
        with self.assertRaises(NotImplementedError):
            self.expt.insert(10)
        self.assertEqual([], level_wise_items(self.expt))

    def test_precedence(self):
        def precedence(operator: str) -> int:
            if operator == '^':
                return 1
            if operator in ('*', '/', '%'):
                return 2
            if operator in ('+', '-'):
                return 3
            return 4

        operators = [
            '^',
            '*', '/', ' %',
            '+', '-',
            '$', '?', '#', '@', '&', '=', '_', '<', '>', '!'
        ]
        for item in operators:
            self.assertEqual(precedence(item),
                             ExpressionTree().precedence_of(item))

    def test_preorder_print(self):
        results = [
            '\na', 'NULL', '\n+'
                           '\n├─▶ 1'
                           '\n└─▶ 2',
            '\n+'
            '\n├─▶ root'
            '\n└─▶ child',

            '\n*'
            '\n├─▶ %'
            '\n│   ├─▶ 1'
            '\n│   └─▶ +'  # Normal ExpressionTree Repr
            '\n│       ├─▶ B'
            '\n│       └─▶ Baxy'
            '\n└─▶ D',

            '\n+'
            '\n├─▶ 1'
            '\n└─▶ b',

            '\n/'
            '\n├─▶ *'
            '\n│   ├─▶ D'
            '\n│   └─▶ +'
            '\n│       ├─▶ 6'
            '\n│       └─▶ A'
            '\n└─▶ C',

            '\n/'
            '\n├─▶ %'
            '\n│   ├─▶ *'
            '\n│   │   ├─▶ A'  # An example of an expression tree
            '\n│   │   └─▶ B'
            '\n│   └─▶ C'
            '\n└─▶ D'
        ]

        for testcase, result in zip(self.print_test_cases, results):
            tree = ExpressionTree(testcase)
            tree.preorder_print()
            self.assertEqual(result, tree._string)

    def test_string_representation(self):
        results = [
            '   a  \n', '  NULL', '      +     \n'
                                  '   ┌──┴──┐  \n'
                                  '   1     2  \n',

            '          +         \n'
            '     ┌────┴────┐    \n'
            '   root      child  \n',

            # Normal ExpressionTree Repr
            f"{' ' * 8}                        *                {' ' * 15}\n"
            f"{' ' * 8}        ┌───────────────┴───────────────┐{' ' * 15}\n"
            f"{' ' * 8}        %                               D{' ' * 15}\n"
            f"{' ' * 8}┌───────┴───────┐                        {' ' * 15}\n"
            f"{' ' * 8}1               +                        {' ' * 15}\n"
            f"{' ' * 8}            ┌───┴───┐                    {' ' * 15}\n"
            f"{' ' * 8}            B     Baxy                   {' ' * 15}\n",

            '      +     \n'
            '   ┌──┴──┐  \n'
            '   1     b  \n',
            '                        /                       \n'
            '            ┌───────────┴───────────┐           \n'
            '            *                       C           \n'
            '      ┌─────┴─────┐                             \n'
            '      D           +                             \n'
            '               ┌──┴──┐                          \n'
            '               6     A                          \n',

            # An example of an expression tree
            '                        /                       \n'
            '            ┌───────────┴───────────┐           \n'
            '            %                       D           \n'
            '      ┌─────┴─────┐                             \n'
            '      *           C                             \n'
            '   ┌──┴──┐                                      \n'
            '   A     B                                      \n',
        ]

        for testcase, result in zip(self.print_test_cases, results):
            tree = ExpressionTree(testcase)
            self.assertEqual(result, tree.__str__())


if __name__ == '__main__':
    unittest.main()
