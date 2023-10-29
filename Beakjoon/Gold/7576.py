from collections import deque

# 상, 하, 좌, 우 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, visited):
    count = 0
    a, b = graph.index(1)
    print(a)

    return 0


m, n = map(int, input().split())
visit = [[0] * m] * n
farm = [[] for _ in range(n)]
for i in range(n):
    farm[i] = list(map(int, input().split()))
print(farm)
bfs(farm, visit)
