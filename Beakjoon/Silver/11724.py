def dfs(graph, start, visited):
    visited[start] = True
    for j in graph[start]:
        if not visited[j]:
            dfs(graph, j, visited)


n, m = map(int, input().split())
edge_info = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    edge_info[u].append(v)
    edge_info[v].append(u)

visit_info = [False] * (n + 1)
count = 0

for i in range(1, n + 1):
    if not visit_info[i]:
        dfs(edge_info, i, visit_info)
        count += 1

print(count)
