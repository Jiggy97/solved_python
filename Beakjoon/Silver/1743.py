import sys

# 최대 재귀 깊이 설정을 높임
sys.setrecursionlimit(10000)

n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = 1

dx = [-1, 1, 0, 0] # 상하좌우 이동하여 계산하기 위한 list
dy = [0, 0, -1, 1]


def dfs(graph, x, y, visited):
    visited[x][y] = True
    count = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 1 and not visited[nx][ny]:
            count += dfs(graph, nx, ny, visited)

    return count


count_list = []
for a in range(n):
    for b in range(m):
        if graph[a][b] == 1 and not visited[a][b]:
            count_list.append(dfs(graph, a, b, visited))

print(max(count_list))
