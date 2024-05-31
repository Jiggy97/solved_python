from collections import deque

m, n, h = map(int, input().split())
day = 0
tomato = []
for _ in range(h):
    floor = []
    for _ in range(n):
        floor.append(list(map(int, input().split())))
    tomato.append(floor)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs(queue, graph):
    d = 0
    while queue:
        a, b, c, d = queue.popleft()
        for i in range(6):
            nx = a + dx[i]
            ny = b + dy[i]
            nz = c + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if graph[nx][ny][nz] == 0:
                    queue.append((nx, ny, nz, d+1))
                    graph[nx][ny][nz] = 1
    return d


ripen_tomato = deque()
for x in range(h):
    for y in range(n):
        for z in range(m):
            if tomato[x][y][z] == 1:
                ripen_tomato.append((x, y, z, 0))

day = bfs(ripen_tomato, tomato)
for f in tomato:
    for r in f:
        if 0 in r:
            print(-1)
            exit()

print(day)
