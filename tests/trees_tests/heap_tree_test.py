from datastax.trees import HeapTree

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
# assert sorted(items) != my, 'Wow, the list is sorted'

# print(H)

MiHT = HeapTree()
print(MiHT)
MiHT.heappush(30)
print(MiHT)
x = MiHT.heappop()
print(x)
print("HEAP MUST BE EMPTY")
print(MiHT)
for item in [*range(9, -1, -1)][::-1]: MiHT.heappush(item)
print(MiHT.preorder_print())
print(MiHT.array_repr)
items = [1, 3, 4, 6, 3, 8, 9, 12, 14, 2]
for item in items:
    MiHT.heappush(item)
    print(MiHT)
    print(MiHT.array_repr)
    print(f"Inserted {item}")

print('############')
print(MiHT)
x = [MiHT.heappop() for i in range(len(MiHT.array_repr))]
print(x)
