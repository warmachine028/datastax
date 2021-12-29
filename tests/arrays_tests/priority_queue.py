from datastax.arrays import PriorityQueue

pq = PriorityQueue(5)
# print()
pq.enqueue(10)
pq.enqueue(20)
pq.enqueue(15)
pq.enqueue(30)
pq.enqueue(40)
print(pq)
# pq.enqueue(-5)
print(pq)
# pq.enqueue(90)
for i in range(10):
    x = pq.dequeue()
    print(f"Popped Element: {x}")
    print(pq)
print(pq)
