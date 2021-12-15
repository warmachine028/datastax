from datastax.trees import AVLTree

avl = AVLTree()
for item in [*range(10)]:
    avl.insert(item)
    print(avl)
# print(avl)
print(AVLTree([10, 9, 8, 7, 2, 1, 99, 18, 17, 25, 23]))
