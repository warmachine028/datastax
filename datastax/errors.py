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
        if data_structure in ['Queue', 'PriorityQueue']: operation = 'ENQUEUE'
        elif data_structure == 'Stack': operation = 'PUSH'
        
        message = f"{data_structure} is already empty, " \
                  f"can't perform {operation} operation any further"
        super().__init__(message)


class UnderFlowError(Error):
    def __init__(self, data_type: Any):
        data_structure = type(data_type).__name__
        operation = ''
        if data_structure in ['Queue', 'PriorityQueue']: operation = 'DEQUEUE'
        elif data_structure == 'Stack': operation = 'POP'
        
        message = f"{data_structure} is already full, " \
                  f"can't perform {operation} operation any further"
        super().__init__(message)
