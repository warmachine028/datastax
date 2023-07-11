# __init__.py
# flake8: noqa
# encoding: utf-8
# module AbstractLists
# from (datastax)

"""
`AbstractLists` is a subPackage which contains logic to handle the string representation of Lists.

- This package is created with the sole purpose of abstracting users from the underlying implementation details and providing a clean and simplified interface.

- The primary objective of this subPackage is to shield users from the intricate functionality and cosmetic logic of the data structures.

- Instead, it focuses on presenting a well-defined and user-friendly representation of the data structures.

- By utilizing the functionalities provided within this directory, users can interact with the data structures effectively without needing to understand the internal workings or cosmetic intricacies.

- The intention is to enhance usability and readability, making it easier for users to utilize and work with the data structures in a straightforward manner.

Through encapsulating the logic and providing a clear separation between the underlying functionality and the user interface, this subPackage promotes code organization and maintainability, ensuring that users can easily employ the data structures without being burdened by the underlying complexity.

Author: Pritam Kundu
Date: 2023-07-10
"""
from .Node import Node
from .DoublyNode import DoublyNode
from .LinkedList import LinkedList
from .DoublyLinkedList import DoublyLinkedList
from .CircularLinkedList import CircularLinkedList
from .DoublyCircularList import DoublyCircularList
from .Queue import Queue

__all__ = [
    'Node',
    'DoublyNode',
    'LinkedList',
    'DoublyLinkedList',
    'CircularLinkedList',
    'DoublyCircularList',
    'Queue'
]
