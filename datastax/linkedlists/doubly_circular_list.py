from typing import Any

from datastax.linkedlists.circular_list import CircularLinkedList
from datastax.linkedlists.doubly_linked_list import DoublyLinkedList, DoublyNode


class DoublyCircularList(DoublyLinkedList, CircularLinkedList):
    def append(self, data: Any) -> None:
        super().append(data)
        self.head.prev, self.tail.next = self.tail, self.head
    
    def insert(self, data: Any) -> None:
        super().insert(data)
        self.head.prev, self.tail.next = self.tail, self.head
    
    def __str__(self, reverse: bool = False, node: DoublyNode = None):
        head = node or (self.tail if reverse else self.head)
        if not head: return "NULL"
        string = f"┌->"
        ref = head
        while True:
            string += f' Node[{str(ref.data)}] <->'
            ref = ref.prev if reverse else ref.next
            if ref is head: break
        string = f"{string[:-1]}┐\n└{'<-->'.center(len(string) - 2, '─')}┘"
        return string


if __name__ == '__main__':
    DCLL = DoublyCircularList([1, 2, 3])
    print(DCLL)
    print(DCLL.__str__(True))
    print(DCLL.__str__(False, DCLL.head.next))
    print(DCLL.__str__(False, DCLL.head.next.next))
    print()
    print(DCLL.__str__(True, DCLL.head.prev))
