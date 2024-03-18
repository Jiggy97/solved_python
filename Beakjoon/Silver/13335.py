from collections import deque

n, w, L = map(int, input().split())
truck_list = list(map(int, input().split()))

queue = deque()
queue.append(truck_list[0])
dis = [0] * n
next = 1
now = 0
time = 0

while queue:
    time += 1
    for i in range(next):
        dis[i] += 1
    if dis[now] == w:
        queue.popleft()
        now += 1
    if next < len(truck_list):
        if L >= sum(queue) + truck_list[next]:
            queue.append(truck_list[next])
            next += 1

print(time + 1)
