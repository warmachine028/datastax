from typing import Any

from datastax.linkedlists.doubly_linked_list import DoublyLinkedList, DoublyNode


class DoublyCircularList(DoublyLinkedList):
    def append(self, data: Any) -> None:
        super().append(data)
        self.head.prev, self.tail.next = self.tail, self.head
    
    def insert(self, data: Any) -> None:
        super().insert(data)
        self.head.prev, self.tail.next = self.tail, self.head
    
    def __str__(self, reverse=False, node: DoublyNode = None):
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
