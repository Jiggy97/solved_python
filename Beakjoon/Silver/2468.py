from collections import deque

n = int(input())
region = []
max_height = []
min_height = []
for _ in range(n):
    row = list(map(int, input().split()))
    max_height.append(max(row))
    min_height.append(min(row))
    region.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b, h, graph, v):
    v[a][b] = True
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > h and not v[nx][ny]:
                v[nx][ny] = True
                queue.append((nx, ny))


result = []
for j in range(max(max_height)):
    count = 0
    visited = [[False] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if region[r][c] > j and not visited[r][c]:
                bfs(r, c, j, region, visited)
                count += 1
    result.append(count)

print(max(result))
