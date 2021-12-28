from datastax.trees.heap_tree import HeapTree, HeapTreeNode


# from heap_tree import HeapTree, HeapTreeNode


class MinHeapTree(HeapTree):
    def heapify(self, node: HeapTreeNode) -> None:
        if node.parent and node.parent.data > node.data:
            node.parent.data, node.data = node.data, node.parent.data
            self.heapify(node.parent)
    
    def shift_up(self, node: HeapTreeNode) -> None:
        root = node
        left_child = root.left
        right_child = root.right
        if left_child and left_child.data < root.data:
            root = left_child
        if right_child and right_child.data < root.data:
            root = right_child
        if root is node: return
        root.data, node.data = node.data, root.data
        self.shift_up(root)
