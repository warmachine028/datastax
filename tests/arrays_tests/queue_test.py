from datastax.arrays import Queue
from datastax.linkedlists import LinkedList

#
q = Queue(2)  # Fixed Size Queue
q.dequeue()  # deletion from empty queue
print(q)
q.enqueue(50)  # inserting in empty queue
print(q)
q.dequeue()
q.enqueue(40)  # inserting in queue with garbage values
print(q)
q.enqueue(60)  # inserting in Queue full with garbage values
q.dequeue()  # deleting from queue with all garbage values
print(q)
q.enqueue(10)  # inserting in queue with all garbage values
print(q)
print("##########################################")
q = Queue()  # Unlimited Size Queue
q.dequeue()  # deletion from empty queue
print(q)
q.enqueue(50)  # inserting in empty queue
print(q)
q.dequeue()
q.enqueue(40)  # inserting in queue with some garbage values
q.dequeue()
print(q)
q.enqueue(60)  # inserting in Queue full with all garbage values
print(q)
q.dequeue()
q.dequeue()  # deleting from queue with all garbage values
print(q)
q.enqueue(10)  # inserting in queue with all garbage values
print(q)


# inserting miscellaneos items in queue
def insert(queue: Queue, item) -> None:
    queue.enqueue(item)
    print(queue)


q = Queue()
insert(q, 1000)  # integer
insert(q, {1, 2, 3, 4, 5, 6, 7})  # set
insert(q, [190, 200, 300])  # list
insert(q, "STRING")  # string
insert(q, "A")  # character
insert(q, {1: 2, 2: 3, 3: 4})  # dictionary
insert(q, LinkedList([1, 2]).head)  # inserting a singly node
insert(q, LinkedList([1, 2]))  # inserting singly linked list
q.dequeue()
print(q)
print(q.array_repr)
