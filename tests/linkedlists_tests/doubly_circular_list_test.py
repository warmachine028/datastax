from datastax.linkedlists import DoublyCircularList

DCLL = DoublyCircularList([1, 2, 3])
print(DCLL)
print(DCLL.__str__(True))
print(DCLL.__str__(False, DCLL.head.next))
print(DCLL.__str__(False, DCLL.head.next.next))
print()
print(DCLL.__str__(True, DCLL.head.prev))
