# AVL Tree Implementation (Also: Self Balancing Binary Tree)
from __future__ import annotations

from typing import Any, Optional

from datastax.trees.binary_search_tree import BinarySearchTree, TreeNode


class AVLNode(TreeNode):
    def __init__(self, data: Any,
                 left: AVLNode = None,
                 right: AVLNode = None,
                 height: int = 1):
        super().__init__(data, left, right)
        self.left = left
        self.right = right
        self.height = height


class AVLTree(BinarySearchTree):
    def __init__(self, array: list[Any] = None, root=None):
        self._root: Optional[AVLNode] = root
        super().__init__(array, root)
    
    def insert(self, data: Any, root: AVLNode = None) -> None:
        def place(parent: Optional[AVLNode]) -> Optional[AVLNode]:
            if not parent: return AVLNode(data)
            elif parent.data < data: parent.right = place(parent.right)
            elif data < parent.data: parent.left = place(parent.left)
            
            parent.height = 1 + max(self.height(parent.left), self.height(parent.right))
            # Balancing the tree
            return self.balance(parent, data)
        
        root = root or self.root
        result = place(root)
        if result and result is not root: self._root = result
    
    def balance(self, parent: Optional[AVLNode], data: Any) -> Optional[AVLNode]:
        if not parent: return None
        balance_factor = self.check_balance_factor(parent)
        if balance_factor < -1:
            if parent.right and parent.right.data < data:  # Perform LL Rotation
                return self.left_rotate(parent)
            else:
                if parent.right: parent.right = self.right_rotate(parent.right)  # Perform RL Rotation
                return self.left_rotate(parent)
        
        if balance_factor > 1:
            if parent.left and data < parent.left.data:
                return self.right_rotate(parent)
            else:
                if parent.left: parent.left = self.left_rotate(parent.left)  # Perform LR Rotation
                return self.right_rotate(parent)
        return parent
    
    def check_balance_factor(self, root: AVLNode = None) -> int:
        def balance_factor(parent: Optional[AVLNode]) -> int:
            return self.height(parent.left) - self.height(parent.right) if parent else 0
        
        return balance_factor(root or self.root)
    
    @staticmethod
    def height(node: Optional[AVLNode]) -> int:
        return node.height if node else 0
    
    def right_rotate(self, node: AVLNode) -> Optional[AVLNode]:
        left = node.left
        if left:
            temp = left.right
            left.right = node
            node.left = temp
            node.height = 1 + max(self.height(node.left), self.height(node.right))
            left.height = 1 + max(self.height(left.left), self.height(left.right))
        return left
    
    def left_rotate(self, node: AVLNode) -> Optional[AVLNode]:
        right = node.right
        if right:
            temp = right.left
            right.left = node
            node.right = temp
            node.height = 1 + max(self.height(node.left), self.height(node.right))
            right.height = 1 + max(self.height(right.left), self.height(right.right))
        return right
