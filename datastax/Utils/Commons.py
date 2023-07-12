from typing import Any


class Commons:
    @staticmethod
    def repr(item: Any) -> str:
        if "\n" in str(item):
            return f"{str(type(item))[8:-2].split('.')[-1]}@{id(item)}"
        return str(item)
