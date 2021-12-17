from datastax.linkedlists import CircularLinkedList

CLL = CircularLinkedList([*range(5)])
CLL.insert(999)
CLL.append("ABQ")
print(CLL.__str__())
print(CLL.__str__(CLL.head.next))
print(CLL.__str__(CLL.head.next.next))
print(CLL.__str__(CLL.head.next.next.next))
print(CLL.__str__(CLL.head.next.next.next.next))
