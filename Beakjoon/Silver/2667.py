from collections import deque

# 상, 하, 좌, 우 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph, visited, n):
    count = 1
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1

    return count

def solution(n, graph):
    visited = [[False] * n for _ in range(n)]
    result = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                result.append(bfs(i, j, graph, visited, n))

    result.sort()
    return result

# 입력 예시
n = int(input())
graph = []
for _ in range(n):
    row = list(map(int, input()))
    graph.append(row)

# 결과 출력
answer = solution(n, graph)
print(len(answer))
for count in answer:
    print(count)
