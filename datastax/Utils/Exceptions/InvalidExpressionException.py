from typing import Any
from .DatastaxException import DatastaxException


class InvalidExpressionException(DatastaxException):
    def __init__(self, data_type: Any = 'ExpressionTree'):
        data_structure = type(data_type).__name__
        message = f"Can't construct {data_structure}. " \
                  "Check if any operands or operators are missing."
        super().__init__(message)
