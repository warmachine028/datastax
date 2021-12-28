from __future__ import annotations

from typing import Optional, Any

from datastax.trees import BinaryTree, TreeNode


class HeapTreeNode(TreeNode):
    def __init__(self, data: Any,
                 left=None,
                 right=None,
                 parent=None,
                 previous_tail=None
                 ) -> None:
        self.parent: HeapTreeNode = parent
        self.prev_leaf: HeapTreeNode = previous_tail
        super().__init__(data, left, right)


class HeapTree(BinaryTree):
    def __init__(self, array: list[Any] = None, root=None):
        self._root: Optional[HeapTreeNode] = root
        self._leaf: Optional[HeapTreeNode] = None
        super().__init__(array, root)
    
    def _construct(self, array: list[Any] = None) -> Optional[HeapTree]:
        if not array or array[0] is None: return None
        for item in array:
            try: self.heappush(item)
            except TypeError as error:
                print(error)
                break
        return self
    
    @property
    def leaf(self):
        return self._leaf
    
    def heapify(self, node: HeapTreeNode) -> None:
        if node.parent and node.parent.data < node.data:
            node.parent.data, node.data = node.data, node.parent.data
            self.heapify(node.parent)
    
    def update_leaf(self, node: HeapTreeNode) -> None:
        # reach extreme left of next level if current level is full
        if node.parent is None: self._leaf = node
        elif node.parent.left is node: self._leaf = node.parent.right
        elif node.parent.right is node: self.update_leaf(node.parent)
        while self.leaf and self.leaf.left:
            self._leaf = self.leaf.left
    
    def heappush(self, data: Any, root=None) -> None:
        root = root or self.root
        node = HeapTreeNode(data)
        if root is None:  # Heap Tree is Empty
            self._root = self._leaf = node
        # Heap tree has nodes,. So inserting new node in the left of leftmost leaf node
        elif self.leaf and self.leaf.left is None:
            self.leaf.left = node
            node.parent = self.leaf
        else:
            if not self.leaf: return
            self.leaf.right = node
            previous_leaf = self.leaf
            node.parent = self.leaf
            self.update_leaf(self.leaf)
            self.leaf.prev_leaf = previous_leaf
        self.heapify(node)
    
    def shift_up(self, node: HeapTreeNode) -> None:
        root = node
        left_child = root.left
        right_child = root.right
        if left_child and left_child.data > root.data:
            root = left_child
        if right_child and right_child.data > root.data:
            root = right_child
        if root is node: return
        root.data, node.data = node.data, root.data
        self.shift_up(root)
        # if node is None or node.left is None:
        #     return
        # maximum = node.left
        # if node.right and maximum.data < node.right.data:
        #     maximum = node.right
        # if maximum.data > node.data:
        #     maximum.data, node.data = node.data, maximum.data
        #     self.shift_up(maximum)
        #
    
    def heappop(self) -> Optional[Any]:
        deleted_data = self.root.data if self.root else None
        if self.root is self.leaf and not any([self.leaf.left, self.leaf.right]):
            self._root = self._leaf = None
        
        else:
            if self.leaf.right and self.root:
                self.root.data = self.leaf.right.data
                self.leaf.right = None
                self.shift_up(self.root)
            elif self.leaf.left and self.root:
                self.root.data = self.leaf.left.data
                self.leaf.left = None
                self.shift_up(self.root)
            else:  # We have reached the end of a level
                self._leaf = self.leaf.prev_leaf
                return self.heappop()
        return deleted_data


if __name__ == '__main__':
    def main():
        items = ['E', 'A', 'G', 'X', 'F', 'D', 'Z', 'B']
        h = HeapTree()
        for item in items:
            h.heappush(item)
            print(h)
        print("########\\SUCCESSFULLY INSERTED/########")
        print(h)
        my = []
        for i in range(8):
            my.append(h.heappop())
            print(my)
            print(h)
            # break
        
        print(my)
        assert sorted(items, reverse=True) != my, 'Wow, the list is sorted reversely'
    
    
    # print(H)
    main()
