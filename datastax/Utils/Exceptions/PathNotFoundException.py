from typing import Any
from .DatastaxException import DatastaxException


class PathNotFoundException(DatastaxException):
    def __init__(self, data_type: Any):
        data_structure = type(data_type).__name__
        message = f"Path doesn't exist in {data_structure}"
        super().__init__(message)
