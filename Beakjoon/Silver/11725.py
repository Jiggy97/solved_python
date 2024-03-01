from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# def dfs(v):
#     for i in graph[v]:
#         if not visited[i]:
#             visited[i] = v
#             dfs(i)


# dfs(1)
def bfs():
    queue = deque()
    queue.append(1)
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if visited[nxt] == 0:
                visited[nxt] = now
                queue.append(nxt)


bfs()
for j in range(2, n + 1):
    print(visited[j])
