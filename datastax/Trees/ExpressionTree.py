from typing import Any, Optional, Self, Sequence

from datastax.Utils.Exceptions import (
    UnmatchedBracketPairException,
    InvalidExpressionException,
    UnderflowException,
    OverflowException
)
from datastax.Arrays import Stack
from datastax.Nodes import TreeNode
from datastax.Trees.BinaryTree import BinaryTree


class ExpressionTree(BinaryTree):
    _infix_expression = ""
    _postfix_expression = ""

    @property
    def infix_expression(self):
        return self._infix_expression

    @property
    def postfix_expression(self):
        return self._postfix_expression

    def __init__(self, infix_expression: Optional[Sequence] = None):
        super().__init__(infix_expression)

    def _construct(self, infix_expression: Optional[Sequence] = None
                   ) -> Optional[Self]:
        if not infix_expression or infix_expression[0] is None:
            return None
        infix_expression = [*filter(lambda x: x is not None, infix_expression)]
        self._set_infix(''.join(map(str, infix_expression)))
        self._set_postfix(self.infix_to_postfix())
        stack = Stack(capacity=len(infix_expression))
        for item in self._postfix_expression.split():
            if self.is_operator(item):
                try:
                    right, left = stack.pop(), stack.pop()
                    node = TreeNode(item, left, right)
                except UnderflowException:
                    raise InvalidExpressionException(self)
            else:
                node = TreeNode(item)
            try:
                stack.push(node)
            except OverflowException:
                raise InvalidExpressionException(self)
        self.set_root(stack.pop())
        return self

    @staticmethod
    def is_operator(character: str) -> bool:
        return True if character in ('+', '-', '*', '/', '^', '%') else False

    @staticmethod
    def precedence_of(operator: str) -> int:
        precedence = {
            '^': 1,
            '*': 2, '/': 2, '%': 2,
            '+': 3, '-': 3
        }
        return precedence.get(operator, 4)

    def infix_to_postfix(self, infix_expression: Optional[str] = '') -> str:
        if not infix_expression:
            infix_expression = self._infix_expression

        if infix_expression.count('(') != infix_expression.count(')'):
            raise UnmatchedBracketPairException(self, infix_expression)

        postfix_expression = ''
        stack = Stack(capacity=len(infix_expression))
        infix_expression += ')'
        stack.push('(')
        current_count = 0
        while current_count < len(infix_expression):
            current_item = infix_expression[current_count]
            if current_item.isalnum():
                while current_item.isalnum():
                    postfix_expression += current_item
                    current_count += 1
                    if current_count >= len(infix_expression):
                        break
                    current_item = infix_expression[current_count]
                postfix_expression += ' '
                continue

            if current_item == '(':
                stack.push(current_item)

            elif current_item == ')':
                while not stack.is_empty():
                    if stack.peek() == '(':
                        stack.pop()
                        break
                    postfix_expression += f'{stack.pop()} '

            elif self.is_operator(current_item):
                while self.is_operator(stack.peek()) and self.precedence_of(
                        current_item) >= self.precedence_of(stack.peek()):
                    postfix_expression += f'{stack.pop()} '
                stack.push(current_item)

            current_count += 1

        return postfix_expression

    def _set_infix(self, infix_expression: str):
        self._infix_expression = infix_expression

    def _set_postfix(self, postfix_expression: str):
        self._postfix_expression = postfix_expression

    def insert(self, item: Any):
        raise NotImplementedError

    def insert_path(self, data: Any, path: Optional[list[str]] = None) -> None:
        raise NotImplementedError
