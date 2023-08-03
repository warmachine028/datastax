from typing import Any
from .DatastaxException import DatastaxException


class UnmatchedBracketPairException(DatastaxException):
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
