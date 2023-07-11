# Expression Tree Implementation
from __future__ import annotations

from typing import Optional, Union, Any

from datastax.Arrays import Stack
from datastax.errors import (
    UnmatchedBracketPairError, InvalidExpressionError,
    UnderFlowError, OverFlowError
)
from datastax.trees.private_trees.binary_tree import TreeNode, BinaryTree


class ExpressionTree(BinaryTree):
    def __init__(self, infix_expression: Union[list, str] = None):
        self.infix_expression = ''
        self.postfix_expression = ''
        super().__init__(infix_expression)

    def _construct(self, infix_expression: Union[list, str] = None
                   ) -> Optional[ExpressionTree]:
        if not infix_expression or infix_expression[0] is None:
            return None
        infix_expression = [*filter(lambda x: x is not None, infix_expression)]
        self.infix_expression = ''.join(map(str, infix_expression))
        self.postfix_expression = self.infix_to_postfix()
        stack = Stack(capacity=len(infix_expression))
        for item in self.postfix_expression.split():
            if self.is_operator(item):
                try:
                    right, left = stack.pop(), stack.pop()
                    node = TreeNode(item, left, right)
                except UnderFlowError:
                    raise InvalidExpressionError(self)
            else:
                node = TreeNode(item)
            try:
                stack.push(node)
            except OverFlowError:
                raise InvalidExpressionError(self)
        self._root = stack.pop()
        return self

    @staticmethod
    def is_operator(character: str) -> bool:
        return True if character in ('+', '-', '*', '/', '^', '%') else False

    @staticmethod
    def precedence_of(operator: str) -> int:
        if operator == '^':
            return 1
        if operator in ('*', '/', '%'):
            return 2
        if operator in ('+', '-'):
            return 3
        return 4

    def infix_to_postfix(self, infix_expression=''):
        if not infix_expression:
            infix_expression = self.infix_expression

        if infix_expression.count('(') != infix_expression.count(')'):
            raise UnmatchedBracketPairError(self, infix_expression)

        postfix_expression: str = ''
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

    def insert(self, item: Any):
        raise NotImplementedError
