import heapq
from collections import deque

INF = int(1e9)

n, k = map(int, input().split())

time = [INF for _ in range(100001)]

queue = deque([])
queue.append((0, n))

while queue:
    dis, now = queue.popleft()

    if now == k:
        break

    if time[now] < dis:
        continue

    if dis < time[now * 2]:
        time[now * 2] = dis
        queue.append((dis, now * 2))

    if dis + 1 < time[now + 1]:
        time[now + 1] = dis + 1
        queue.append((dis + 1, now + 1))

    if now - 1 >= 0 and dis + 1 < time[now - 1]:
        time[now - 1] = dis + 1
        queue.append((dis + 1, now - 1))

print(time[k])

# if n <= k:
#     time = [INF for _ in range(k + 1)]
# else:
#     time = [INF for _ in range(n + 1)]
#
#
# def dijkstra(start, end):
#     queue = []
#     heapq.heappush(queue, (0, start))
#     time[start] = 0
#
#     while queue:
#         dist, now = heapq.heappop(queue)
#
#         if time[now] < dist:
#             continue
#
#         if now * 2 <= end and dist < time[now * 2]:
#             time[now * 2] = dist
#             heapq.heappush(queue, (dist, now * 2))
#
#         if now + 1 <= end and dist + 1 < time[now + 1]:
#             time[now + 1] = dist + 1
#             heapq.heappush(queue, (dist + 1, now + 1))
#
#         if now - 1 >= 0 and dist + 1 < time[now - 1]:
#             time[now - 1] = dist + 1
#             heapq.heappush(queue, (dist + 1, now - 1))


# dijkstra(n, k)
# print(time[k])
