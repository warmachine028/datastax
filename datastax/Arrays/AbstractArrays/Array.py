from abc import ABC as AbstractClass, abstractmethod
from sys import maxsize
from typing import Any


class Array(AbstractClass):
    _capacity = 0
    _array: list[Any] = []

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def array(self) -> list[Any]:
        return self._array

    def set_capacity(self, capacity: int | None) -> None:
        if capacity is None:
            self._capacity = maxsize
            return
        if not isinstance(capacity, int):
            raise TypeError("The 'capacity' parameter must be an "
                            "instance of int or its subclass.")
        if capacity < 0:
            raise ValueError("Capacity can't be negative")
        self._capacity = capacity

    @abstractmethod
    def append(self, data: Any) -> None:
        ...

    @abstractmethod
    def insert(self, data: Any) -> None:
        ...

    @abstractmethod
    def pop(self) -> Any:
        ...
