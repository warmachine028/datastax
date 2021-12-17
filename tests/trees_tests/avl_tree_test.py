from datastax.trees import AVLTree

avl = AVLTree()
for item in [*range(10)]:
    avl.insert(item)
    print(avl)
# print(avl)
print(AVLTree([10, 9, 8, 7, 2, 1, 99, 18, 17, 25, 23]))
print(AVLTree([10, [1, 2, 3]]))
print(AVLTree([[2, 3], [1, 2, 3], [1, 3, 2]]))
print(AVLTree([1, 1, 1]))

avt = AVLTree([*range(1, 8)])
avt.insert(9)
avt.insert(7.5)
avt.insert(8.5)
print(avt)
print(avt.array_repr)
