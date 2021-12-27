from datastax.trees import MaxHeapTree

MHT = MaxHeapTree()
print(MHT)
MHT.heappush(30)
print(MHT)
x = MHT.heappop()
print(x)
print("HEAP MUST BE EMPTY")
print(MHT)
MHT.heapify([*range(9, -1, -1)][::-1])
print(MHT.preorder_print())
print(MHT.array_repr())
items = [1, 3, 4, 6, 3, 8, 9, 12, 14, 2]
for item in items:
    MHT.heappush(item)
    print(MHT)
    print(MHT.array_repr())
    print(f"Inserted {item}")
