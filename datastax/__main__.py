import sys

from datastax import Lists, trees, Arrays


def main():
    if len(sys.argv) > 1:
        data_structure = sys.argv[1].lower()
        # take User given data or default
        data = sys.argv[2:] if len(sys.argv) > 2 else [*range(5)]
        if data_structure in ('array', 'arrays'):
            queue = Arrays.Queue(capacity=len(data))
            stack = Arrays.Stack(capacity=len(data))
            p_queue = Arrays.PriorityQueue(capacity=len(data))
            for i in data:
                stack.push(i)
                queue.enqueue(i)
                p_queue.enqueue(i)
            print("Visuals for Arrays:\n\n"
                  f"1. Stack: \n"
                  f"{stack}\n\n"
                  f"2. Queue: \n"
                  f"{queue}\n\n"
                  f"3. Priority Queue: \n"
                  f"{p_queue}\n\n")
        elif data_structure in ('linkedlist', "linkedlists"):
            print("Visuals for LinkedLists:\n\n"
                  f"1. Linked List: \n"
                  f"{Lists.LinkedList(data)}\n\n"
                  f"2. Doubly Linked List: \n"
                  f"{Lists.DoublyLinkedList(data)}\n\n"
                  f"3. Circular Linked List: \n"
                  f"{Lists.CircularLinkedList(data)}\n\n"
                  f"4. Doubly Circular List: \n"
                  f"{Lists.DoublyCircularList(data)}\n\n"
                  f"5. Queue: \n"
                  f"{Lists.Queue(None, data)}\n\n"
                  f"6. LRU Cache: \n"
                  f"{Lists.LRUCache(capacity=10)}\n\n"
                  )
        elif data_structure in ('tree', 'trees'):
            print("Visuals for Trees:\n\n"
                  f"1. Binary Tree \n"
                  f"{trees.BinaryTree(data)}\n\n"
                  f"2. Binary Search Tree \n"
                  f"{trees.BinarySearchTree(data)}\n\n"
                  f"3. AVL Tree \n"
                  f"{trees.AVLTree(data)}\n\n")
        else:
            print("This module is not available yet")
    else:
        print("$ py datastax <data-structure> [data]\n"
              "Data Structures: \n"
              "->  trees          Hierarchical DS\n"
              "->  lists          Linear DS\n"
              "->  arrays         Fixed Size Linear DS")


if __name__ == '__main__':
    main()
