from collections import deque

T = int(input())
t_list = []

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]


def bfs(goal_x, goal_y, start_x, start_y, length, graph):
    queue = deque()
    queue.append((start_x, start_y))
    if start_x == goal_x and start_y == goal_y:
        return 0

    while queue:
        sx, sy = queue.popleft()
        for i in range(8):
            nx, ny = sx + dx[i], sy + dy[i],
            if nx == goal_x and ny == goal_y:
                graph[nx][ny] = graph[sx][sy]
                return graph[nx][ny]
            if 0 <= nx < length and 0 <= ny < length and graph[nx][ny] == 0:
                graph[nx][ny] = graph[sx][sy] + 1
                queue.append((nx, ny))


for _ in range(T):
    l = int(input())
    chess = [[0] * l for _ in range(l)]
    visited = [[False] * l for _ in range(l)]

    x, y = map(int, input().split())
    gx, gy = map(int, input().split())

    chess[x][y] = 1
    print(bfs(gx, gy, x, y, l, chess))
