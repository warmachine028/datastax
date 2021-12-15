# AVL Tree Implementation (Also: Self Balancing Binary Tree)
from __future__ import annotations

from typing import Any, Optional

from datastax.trees.binary_search_tree import BinarySearchTree, TreeNode


class AVLTreeNode(TreeNode):
    def __init__(self, data: Any, left: AVLTreeNode = None, right: AVLTreeNode = None, height: int = 1) -> None:
        super().__init__(data, left, right)
        self.height = height


class AVLTree(BinarySearchTree):
    def insert(self, data: Any, root: AVLTreeNode = None) -> None:
        def place(parent: Optional[AVLTreeNode]) -> AVLTreeNode:
            if not parent: return AVLTreeNode(data)
            elif parent.data < data: parent.right = place(parent.right)
            elif data < parent.data: parent.left = place(parent.left)
            
            parent.height = 1 + max(self.height(parent.left), self.height(parent.right))
            # Balancing the tree
            return self.balance(parent, data)
        
        root = root or self.root
        result = place(root)
        if result is not root: self._root = result
    
    def balance(self, parent: AVLTreeNode, data: Any) -> AVLTreeNode:
        balance_factor = self.check_balance_factor(parent)
        if balance_factor < -1:
            if parent.right.data < data:  # Perform LL Rotation
                return self.left_rotate(parent)
            else:
                parent.right = self.right_rotate(parent.right)  # Perform RL Rotation
                return self.left_rotate(parent)
        
        if balance_factor > 1:
            if data < parent.left.data:
                return self.right_rotate(parent)
            else:
                parent.left = self.left_rotate(parent.left)  # Perform LR Rotation
                return self.right_rotate(parent)
        return parent
    
    def check_balance_factor(self, root: AVLTreeNode = None) -> int:
        def balance_factor(parent: Optional[AVLTreeNode]) -> int:
            return self.height(parent.left) - self.height(parent.right) if parent else 0
        
        return balance_factor(root or self.root)
    
    @staticmethod
    def height(node: Optional[AVLTreeNode]) -> int:
        return node.height if node else 0
    
    def right_rotate(self, node: AVLTreeNode) -> AVLTreeNode:
        left = node.left
        temp = left.right
        left.right = node
        node.left = temp
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        left.height = 1 + max(self.height(left.left), self.height(left.right))
        return left
    
    def left_rotate(self, node: AVLTreeNode) -> AVLTreeNode:
        right = node.right
        temp = right.left
        right.left = node
        node.right = temp
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        right.height = 1 + max(self.height(right.left), self.height(right.right))
        return right
