from collections import deque

n = int(input())
picture = []
visited = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

print(visited)
for _ in range(n):
    picture.append(input())
print(picture)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b, g, v, c):
    queue = deque([(a, b)])
    v[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if g[nx][ny] == c and not v[nx][ny]:
                    queue.append((nx, ny))
                    v[nx][ny] = True


count1, count2 = 0, 0
for j in range(n):
    for k in range(n):
        if not visited[j][k]:
            bfs(j, k, picture, visited, picture[j][k])
            count1 += 1

picture2 = []
for row in picture:
    tmp = ''
    for idx in row:
        if idx == 'R':
            idx = 'G'
        tmp += idx
    picture2.append(tmp)
print(picture2)

for j in range(n):
    for k in range(n):
        if not visited2[j][k]:
            bfs(j, k, picture2, visited2, picture2[j][k])
            count2 += 1

print(count1, end=' ')
print(count2)







