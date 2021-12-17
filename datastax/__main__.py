import sys

from datastax import linkedlists as ll, trees


def main():
    if len(sys.argv) > 1:
        data_structure = sys.argv[1].lower()
        data = sys.argv[2:] if len(sys.argv) > 2 else [*range(5)]  # take User given data or default
        if data_structure in ('linkedlist', "linkedlists"):
            print("Visuals for LinkedLists:\n\n"
                  f"1. Singly Linked List: \n{ll.LinkedList(data)}\n\n"
                  f"2. Doubly Linked List: \n{ll.DoublyLinkedList(data)}\n\n"
                  f"3. Circular Linked List: \n{ll.CircularLinkedList(data)}\n\n"
                  f"4. Doubly Circular List: \n{ll.DoublyCircularList(data)}\n\n")
        elif data_structure in ('tree', 'trees'):
            print("Visuals for Trees:\n\n"
                  f"1. Binary Tree \n{trees.BinaryTree(data)}\n\n"
                  f"2. Binary Search Tree \n{trees.BinarySearchTree(data)}\n\n"
                  f"3. AVL Tree \n{trees.AVLTree(data)}\n\n")
        else:
            print("This module is not available yet")
    else:
        print("Available modules are:\n"
              "1. LinkedLists\n"
              "2. Trees\n"
              "\nUsage\n"
              "$ py datastax <data-structure> [data]\n"
              "Data Structures: \n"
              "  trees          Hierarchical DS\n"
              "  linkedlists    Linear DS")


if __name__ == '__main__':
    main()
