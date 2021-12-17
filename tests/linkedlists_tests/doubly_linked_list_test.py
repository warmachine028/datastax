from datastax.linkedlists import DoublyLinkedList

DLL = DoublyLinkedList([*range(5)])
print("head -> ", DLL.head)  # head ->  NULL ⟺ Node[0] ⟺ Node[1]

DLL.insert(10)
DLL.insert(20)
DLL.append(199)
print(DLL)
# NULL <-> Node[20] <-> Node[10] <-> Node[0] <-> Node[1] <-> Node[2] <-> Node[3] <-> Node[4] <-> Node[199] <-> NULL
print(DLL.__str__(True))
# NULL <-> Node[199] <-> Node[4] <-> Node[3] <-> Node[2] <-> Node[1] <-> Node[0] <-> Node[10] <-> Node[20] <-> NULL
