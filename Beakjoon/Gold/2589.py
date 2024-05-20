from collections import deque

W, L = map(int, input().split())

treasure_map = []
for _ in range(W):
    treasure_map.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    visited[a][b] = 1
    queue = deque([])
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < W and 0 <= ny < L:
                if visited[nx][ny] == 0 and treasure_map[nx][ny] == 'L':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


dis = []
for i in range(W):
    for j in range(L):
        tmp = []
        if treasure_map[i][j] == 'L':
            visited = [[0] * L for _ in range(W)]
            bfs(i, j)
            for v in visited:
                tmp.append(max(v))
            dis.append(max(tmp))

print(max(dis) - 1)
