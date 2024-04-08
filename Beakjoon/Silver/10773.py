from collections import deque

k = int(input())
result = 0
queue = deque()
for _ in range(k):
    value = int(input())
    if value != 0:
        queue.append(value)
    else:
        queue.pop()
print(sum(queue))
