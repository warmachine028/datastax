# Binary Tree Implementation
from __future__ import annotations

import math
from queue import Queue
from typing import Any, Optional


def node_builder(data: Optional[str], piece_width: int) -> str:
    value: str = data or ''
    gap1 = int(math.ceil(piece_width / 2 - len(value) / 2))
    gap2 = int(math.floor(piece_width / 2 - len(value) / 2))
    return f"{' ' * gap1}{value}{' ' * gap2}"


class TreeNode:
    def __init__(self, data: Any,
                 left=None,
                 right=None) -> None:
        self.left = left
        self.data = data
        self.right = right
    
    def __str__(self):
        values = [self.data, self.left.data if self.left else None, self.right.data if self.right else None]
        values = list(map(lambda value: str(value) if value else "", values))
        max_width = max(len(data) for data in values if data)
        if max_width % 2: max_width += 1  # To make max_width even
        
        "Building string from calculated values"
        per_piece = 2 * (max_width + 4)
        string_builder = f"{node_builder(values[0], per_piece)}\n"
        per_piece //= 2
        hpw = int(per_piece // 2 - 1)
        if any(values[1:]):
            if all(values[1:]):
                string_builder += f"{' ' * (hpw + 1)}┌{'─' * hpw}┴{'─' * hpw}┐\n"
                string_builder += node_builder(values[1], per_piece) + node_builder(values[2], per_piece)
            elif values[1]:
                string_builder += f"{' ' * (hpw + 1)}┌{'─' * hpw}┘\n"
                string_builder += node_builder(values[1], per_piece)
            else:
                string_builder += f"{' ' * (per_piece - 1)} └{'─' * hpw}┐\n"
                string_builder += f"{' ' * (per_piece - 1)} {node_builder(values[2], per_piece)}"
        
        return string_builder
    
    def preorder_print(self) -> str:
        values = [self.data, self.left.data if self.left else None, self.right.data if self.right else None]
        values = list(map(lambda value: str(value) if value else "", values))
        
        string_builder = f'{values[0]}\n'
        if any(values[1:]):
            if all(values[1:]):
                string_builder += f"├─▶ {values[1]}\n"
                string_builder += f"└─▶ {values[2]}"
            else:
                string_builder += f"└─▶ {values[1] or values[2]}"
        
        return string_builder
    
    def __repr__(self): return self.__str__()


class BinaryTree:
    def __init__(self, array: list[Any] = None, root=None):
        self._root = root
        self._construct(array)
        self.__string: Optional[str] = None
    
    @property
    def root(self):
        return self._root
    
    @property  # Level Order Traversal -> Tree to array
    def array_repr(self) -> list[Any]:
        array = []
        queue: Queue[TreeNode] = Queue()
        if self.root: queue.put(self.root)
        while not queue.empty():
            node = queue.get()
            array.append(node.data)
            if node.left: queue.put(node.left)
            if node.right: queue.put(node.right)
        
        return array
    
    def insert_path(self, data: Any, path: list[str] = None) -> None:
        node = TreeNode(data)
        if not self._root:
            self._root = node
            return
        if not path:
            print("Path required for non root nodes")
            return
        parent = self._root
        for direction in path[:-1]:  # Reaching
            if direction == 'left' and parent.left:
                parent = parent.left
            elif direction == 'right' and parent.right:
                parent = parent.right
            else:
                print("Path doesn't exist")
                return
        if path[-1] == 'right' and not parent.right: parent.right = node
        elif path[-1] == 'left' and not parent.left: parent.left = node
        else: print("Place already occupied")
    
    # Helper function to construct tree by level order -> Array to tree
    def _construct(self, array: list[Any] = None) -> Optional[BinaryTree]:
        if not array or array[0] is None: return None
        
        queue: Queue[TreeNode] = Queue(len(array))
        current = 1
        root = TreeNode(array[0])
        queue.put(root)
        while not queue.empty() and current < len(array):
            node = queue.get()
            node.left = None if array[current] is None else TreeNode(array[current])
            if node.left: queue.put(node.left)  # Inserting Left Node
            current += 1
            
            if current >= len(array): break
            
            node.right = None if array[current] is None else TreeNode(array[current])
            if node.right: queue.put(node.right)  # Inserting Right Node
            current += 1
        self._root = root
        return self
    
    # Level order Traversal of Tree
    def __str__(self, root: TreeNode = None):
        root = root or self.root
        if not root: return "  NULL"
        
        lines: list[list[Optional[str]]] = []
        level: list[Optional[TreeNode]] = [root]
        nodes: int = 1
        max_width: int = 0
        while nodes:
            line: list[Optional[str]] = []
            next_level: list[Optional[TreeNode]] = []
            nodes = 0
            for node in level:
                if node:
                    data = str(node.data)
                    max_width = max(len(data), max_width)
                    line.append(data)
                    next_level += [node.left, node.right]
                    if node.left: nodes += 1
                    if node.right: nodes += 1
                    continue
                line.append(None)
                next_level += [None] * 2
            if max_width % 2: max_width += 1
            lines.append(line)
            level = next_level
        
        ##################################################################
        "Building string from calculated values"
        per_piece = len(lines[-1]) * (max_width + 4)
        string_builder = f"{node_builder(lines[0][0], per_piece)}\n"
        per_piece //= 2
        for _, line in enumerate(lines[1:], 1):
            hpw = int(math.floor(per_piece / 2) - 1)
            # Printing ┌ ┴ ┐ or ┌ ─ ┘ or └ ─ ┐ components
            for j, value in enumerate(line):
                string_builder += (
                    ('┴' if value else '┘') if line[j - 1] else ('└' if value else ' ')) if j % 2 else ' '
                
                if not value:
                    string_builder += ' ' * (per_piece - 1)
                    continue
                string_builder += f"{'─' * hpw}┐{' ' * hpw}" if j % 2 else f"{' ' * hpw}┌{'─' * hpw}"
            string_builder += '\n'
            
            # Printing the value of each Node
            for value in line: string_builder += node_builder(value, per_piece)
            string_builder += '\n'
            per_piece //= 2
        
        return string_builder
    
    # Pre Order Traversal of Tree
    def preorder_print(self, root: TreeNode = None) -> str:
        def string_builder(parent: Optional[TreeNode], has_right_child: bool, padding="", component="") -> None:
            if not parent: return
            if self.__string is not None: self.__string += f"\n{padding}{component}{parent.data}"
            if parent is not root: padding += "│   " if has_right_child else "   "
            left_pointer, right_pointer = "├─▶ " if parent.right else "└─▶ ", "└─▶ "
            string_builder(parent.left, bool(parent.right), padding, left_pointer)
            string_builder(parent.right, False, padding, right_pointer)
        
        root = root or self.root
        if not root: return "NULL"
        self.__string = ""
        string_builder(root, bool(root.right))
        return self.__string
    
    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    # Usage
    Tree = BinaryTree([1, 2, 3, 4])
    print(Tree)
    print(Tree.preorder_print())
    print(Tree.array_repr)
    print(Tree.root)
