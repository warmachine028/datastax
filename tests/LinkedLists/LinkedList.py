from typing import Any

from datastax.linkedlists import LinkedList


def test(array: list[Any] = None) -> None:
    ll = LinkedList(array)
    print(f"Head: {ll.head}")  # printing head
    print(ll)  # Printing linkedList itself


test([*range(10)])
test()  # constructing with nothing
test([])  # constructing with empty list
test([None])  # constructing wih a null value
test([None, 1, 2, 3, 4, 5])  # constructing with values where first item being NULL
#########################
L = LinkedList([1, 2, 3, 4, 5, 6])  # Insertion inside filled list
L.insert(10)  # Insertion at the front
L.append(100)  # Insertion at the back
print(L)
######################
L = LinkedList()  # Insertion inside empty list
L.insert(1)  # Insertion at the front
L.append(2)  # Insertion at the back
print(L)
