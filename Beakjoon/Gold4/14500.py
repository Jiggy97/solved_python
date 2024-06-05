N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

maximum = 0


def dfs(x, y, tmp, cnt):
    global maximum
    if cnt == 4:
        maximum = max(maximum, tmp)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
            continue
        visited[nx][ny] = True
        dfs(nx, ny, tmp + graph[nx][ny], cnt + 1)
        visited[nx][ny] = False


def fy(x, y, tmp):
    global maximum
    arr = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        arr.append(graph[nx][ny])
    length = len(arr)
    if length == 4:
        arr.sort(reverse=True)
        arr.pop()
        maximum = max(maximum, sum(arr) + graph[x][y])
    elif length == 3:
        maximum = max(maximum, sum(arr) + graph[x][y])
    return


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, graph[i][j], 1)
        fy(i, j, graph[i][j])
        visited[i][j] = False

print(maximum)
