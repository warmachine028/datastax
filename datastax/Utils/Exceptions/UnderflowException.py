from typing import Any
from .DatastaxException import DatastaxException


class UnderflowException(DatastaxException):
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
