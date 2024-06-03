import copy
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph):
    counts = 0
    queue = deque([])
    for i in virus_idx:
        queue.append(i)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if -1 < nx < N and -1 < ny < M and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 2

    for j in graph:
        for k in j:
            if k == 0:
                counts += 1

    return counts


N, M = map(int, input().split())
lab = []
virus_idx = []
wall_idx = []
for r in range(N):
    col = list(map(int, input().split()))
    for c in range(len(col)):
        if col[c] == 2:
            virus_idx.append((r, c))
        if col[c] == 1:
            wall_idx.append((r, c))
    lab.append(col)

safe_area = 0
for i_1 in range(N):
    for j_1 in range(M):
        if (i_1, j_1) in virus_idx or (i_1, j_1) in wall_idx:
            continue
        for i_2 in range(N):
            for j_2 in range(M):
                if i_2 == i_1 and j_2 == j_1:
                    continue
                if (i_2, j_2) in virus_idx or (i_2, j_2) in wall_idx:
                    continue
                for i_3 in range(N):
                    for j_3 in range(M):
                        if (i_3 == i_2 and j_3 == j_2) or (i_3 == i_1 and j_3 == j_1):
                            continue
                        if (i_3, j_3) in virus_idx or (i_3, j_3) in wall_idx:
                            continue
                        tmp_lab = copy.deepcopy(lab)
                        tmp_lab[i_1][j_1], tmp_lab[i_2][j_2], tmp_lab[i_3][j_3] = 1, 1, 1
                        tmp = bfs(tmp_lab)
                        if tmp > safe_area:
                            safe_area = tmp

print(safe_area)
