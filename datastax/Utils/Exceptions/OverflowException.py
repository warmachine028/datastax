from typing import Any
from .DatastaxException import DatastaxException


class OverflowException(DatastaxException):
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
