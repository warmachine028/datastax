from datastax.arrays import Stack

s = Stack(2)  # Fixed size stack
print(s)  # printing empty stack
s.pop()  # deleting from empty stack
for i in range(2): s.push(10)
print(s)
s.push(1)  # inserting inside full stack
s.pop()  # deleting from full stack
s = Stack()
for i in range(10):
    print(f"Stack is {len(s.array) / s.capacity:.2%} full")
    print(s)
    s.push(i)
print(s)
for i in range(19):
    s.pop()
    print("AFTER POPPING\n", s, sep='')
