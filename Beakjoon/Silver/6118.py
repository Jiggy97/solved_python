from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(s, g, v):
    queue = deque()
    queue.append(s)
    v[s - 1] = 1
    while queue:
        now = queue.popleft()
        for i in g[now]:
            if v[i - 1] == 0:
                v[i - 1] = v[now - 1] + 1
                queue.append(i)


bfs(1, graph, visited)
max_dis = max(visited)
min_idx = []
for j in range(len(visited)):
    if visited[j] == max_dis:
        min_idx.append(j)

idx = min(min_idx)
print(idx + 1, end=' ')
print(visited[idx] - 1, end=' ')
print(len(min_idx))
