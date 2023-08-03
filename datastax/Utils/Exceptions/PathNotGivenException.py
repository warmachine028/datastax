from typing import Any
from .DatastaxException import DatastaxException


class PathNotGivenException(DatastaxException):
    def __init__(self, data_type: Any):
        data_structure = type(data_type).__name__
        message = f"{data_structure} already contains root node. Path " \
                  f"required for inserting non root nodes in tree"
        super().__init__(message)
