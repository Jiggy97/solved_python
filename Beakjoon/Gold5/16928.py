from collections import deque

n, m = map(int, input().split())

visited = [-1] * 101

ladder = {}
snake = {}

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v


def bfs():
    queue = deque([(1, 0)])
    visited[1] = 0

    while queue:
        position, count = queue.popleft()

        for k in range(1, 7):
            next_position = position + k
            if next_position > 100:
                continue

            if next_position in ladder:
                next_position = ladder[next_position]
            elif next_position in snake:
                next_position = snake[next_position]

            if visited[next_position] == -1 or visited[next_position] > count + 1:
                visited[next_position] = count + 1
                queue.append((next_position, count + 1))

            if next_position == 100:
                return visited[next_position]


print(bfs())
