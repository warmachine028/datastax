# from datastax import linkedlists as ll, trees, arrays
from typing import Any


class Error(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class OverFlowError(Error):
    def __init__(self, data_type: Any):
        data_structure = type(data_type).__name__
        operation = ''
        if data_structure in ['Queue', 'PriorityQueue']:
            operation = 'ENQUEUE'
        elif data_structure == 'Stack':
            operation = 'PUSH'

        message = f"{data_structure} is already full, " \
                  f"can't perform {operation} operation any further"
        super().__init__(message)


class UnderFlowError(Error):
    def __init__(self, data_type: Any):
        data_structure = type(data_type).__name__
        operation = ''
        if data_structure in ['Queue', 'PriorityQueue']:
            operation = 'DEQUEUE'
        elif data_structure == 'Stack':
            operation = 'POP'

        message = f"{data_structure} is already empty, " \
                  f"can't perform {operation} operation any further"
        super().__init__(message)


class PathNotGivenError(Error):
    def __init__(self, data_type: Any):
        data_structure = type(data_type).__name__
        message = f"{data_structure} already contains root node. Path " \
                  f"required for inserting non root nodes in tree"
        super().__init__(message)


class PathNotFoundError(Error):
    def __init__(self, data_type: Any):
        data_structure = type(data_type).__name__
        message = f"Path doesn't exist in {data_structure}"
        super().__init__(message)


class InvalidExpressionError(Error):
    def __init__(self, data_type: Any = 'ExpressionTree'):
        data_structure = type(data_type).__name__
        message = f"Can't construct {data_structure}. " \
                  "Check if any operands or operators are missing."
        super().__init__(message)


class UnmatchedBracketPairError(Error):
    def __init__(self, data_type: Any, expression: str):
        data_structure = type(data_type).__name__

        message = f"Can't construct {data_structure}. " \
                  f"Bracket Pairs not matching in {expression}. "
        # Bracket was not closed
        if expression.count('(') > expression.count(')'):
            message += "'(' was never closed."
        # Bracket pairs don't match
        else:
            message += "')' has no pair '('."

        super().__init__(message)


class PathAlreadyOccupiedWarning(UserWarning):
    pass


class NodeNotFoundWarning(UserWarning):
    pass


class DuplicateNodeWarning(UserWarning):
    pass


class DeletionFromEmptyTreeWarning(UserWarning):
    pass


class ExplicitInsertionWarning(UserWarning):
    pass
