from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(start):
    queue = deque([start])
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    count = 1

    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if visited[nxt] == False:
                visited[nxt] = True
                queue.append(nxt)
                count += 1

    return count


count_hacking = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    count_hacking[i] = bfs(i)

max_hacking = max(count_hacking)
for j in range(1, n + 1):
    if count_hacking[j] == max_hacking:
        print(j, end=' ')
