from collections import deque

# 상, 하, 좌, 우 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, visited, start_queue):
    queue = deque([])
    for spot in start_queue:
        queue.append(spot)

    while queue:
        x, y = queue.popleft()

        for go in range(4):
            nx = x + dx[go]
            ny = y + dy[go]

            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph[0]):
                continue

            if graph[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1

    return graph


m, n = map(int, input().split())
visit = [[False] * m for _ in range(n)]
farm = [[] for _ in range(n)]
have_tomato = []
for i in range(n):
    row = list(map(int, input().split()))
    if 1 in row:
        have_tomato.append(i)
    farm[i] = row

# 원래 코드 이렇게 하니까 틀림;
# start_index = []
# for j in have_tomato:
#     start_index.append((j, farm[j].index(1)))

# 아래는 수정 후 코드
start_index = []
for j in have_tomato:
    for k, val in enumerate(farm[j]):
        if val == 1:
            start_index.append((j, k))

result = bfs(farm, visit, start_index)

# 원래 코드 이렇게 하니까 틀림;
# for clear in result:
#     if 0 in clear:
#         result = 0
#         break
#
# if result == 0:
#     print(-1)
# else:
#     print(max(max(result)) - 1)

# 아래는 수정 후 코드
unripe_tomatoes_exist = False
for row in result:
    if 0 in row:
        unripe_tomatoes_exist = True
        break

if unripe_tomatoes_exist:
    print(-1)
else:
    max_day = max(max(row) for row in result)
    print(max_day - 1)