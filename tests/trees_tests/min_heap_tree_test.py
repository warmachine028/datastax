from datastax.trees import MinHeapTree

MiHT = MinHeapTree()
print(MiHT)
MiHT.heappush(30)
print(MiHT)
x = MiHT.heappop()
print(x)
print("HEAP MUST BE EMPTY")
print(MiHT)
MiHT.heapify([*range(9, -1, -1)][::-1])
print(MiHT.preorder_print())
print(MiHT.array_repr())
items = [1, 3, 4, 6, 3, 8, 9, 12, 14, 2]
for item in items:
    MiHT.heappush(item)
    print(MiHT)
    print(MiHT.array_repr())
    print(f"Inserted {item}")

print('############')
print(MiHT)
x = [MiHT.heappop() for i in range(len(MiHT.array_repr()))]
print(x)
