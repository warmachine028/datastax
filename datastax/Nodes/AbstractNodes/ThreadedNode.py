from datastax.Utils import Commons
from datastax.Nodes.AbstractNodes.TreeNode import TreeNode
from abc import ABC as AbstractClass, abstractmethod


class ThreadedNode(TreeNode, AbstractClass):
    _left_is_child: bool
    _right_is_child: bool

    @property
    def left_is_child(self):
        return self._left_is_child

    @property
    def right_is_child(self):
        return self._right_is_child

    def __str__(self):
        values = [
            self.data if self.data is not None else str(None),
            self.left.data if self.left else None,
            self.right.data if self.right else None
        ]
        values = list(
            map(lambda value: Commons.repr(value), values)
        )
        max_width = max(len(Commons.repr(data)) for data in values if data)
        if max_width % 2:
            max_width += 1  # To make max_width even

        padding = 6
        per_piece = 2 * (max_width + padding)
        # Building the part first
        wpn = per_piece // 2 - 1
        wpn = (wpn + 1) if wpn % 2 else wpn
        piece = '┴'.center(wpn, '─')
        piece = f"{'┌' if self.left_is_child else '└'}{piece[:-1]}"
        piece = f"{piece}{'┐' if self.right_is_child else '┘'}"
        piece = f"{piece.center(wpn)}\n"

        root = values[0]
        left = f"{values[1]}"
        right = f"{values[2].center(wpn + 1)}\n"

        if self.left_is_child:
            if self.right_is_child:
                string_builder = (
                        f"{root.center(wpn - 1)}".center(per_piece) +
                        f"\n{piece}{left}{right}"
                )
            else:
                string_builder = (
                        f"{' ' * len(left)}\n"
                        f"{root.center(wpn)}".center(wpn - 1) +
                        f"│\n{piece}"
                        f"{left}"
                )
        else:
            string_builder = left
            if self.right_is_child:
                string_builder = (
                        f"\n│{root.center(wpn)}".center(per_piece) +
                        f"\n{piece}{' ' * len(left)}"
                        f"\n{' ' * len(left)}{right}"
                )
            else:
                string_builder = (
                        f"{right}"
                        f"│{root.center(wpn - 1)}│".center(per_piece) +
                        f"\n{piece}"
                )

        return string_builder

    def preorder_print(self) -> None:
        values = [
            self.data if self.data is not None else str(None),
            self.left.data if self.left else None,
            self.right.data if self.right else None
        ]
        values = list(
            map(
                lambda value: str(value) if value is None else Commons.repr(
                    value
                ),
                values
            )
        )

        string_builder = f'{values[0]}\n'
        if any(values[1:]):
            if all(values[1:]):
                string_builder += f"├─▶ {values[1]}\n"
                string_builder += f"└─▶ {values[2]}"
            else:
                string_builder += f"└─▶ {values[1] or values[2]}"

        print(string_builder)

    @abstractmethod
    def set_left_is_child(self, is_child: bool):
        ...

    @abstractmethod
    def set_right_is_child(self, is_child: bool):
        ...
