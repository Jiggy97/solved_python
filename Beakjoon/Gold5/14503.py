n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))
clean_square = 0
# 북 : 0 / 동 : 1 / 남 : 2 / 서 : 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def clean_room(x, y, z):
    global clean_square
    if room[x][y] == 0:
        room[x][y] = 2
        clean_square += 1

    for _ in range(4):
        z = (z + 3) % 4
        nx = dx[z] + x
        ny = dy[z] + y
        if 0 <= nx < n and 0 <= ny < m:
            if room[nx][ny] == 0:
                clean_room(nx, ny, z)
                return

    nx, ny = x - dx[z], y - dy[z]
    if 0 <= nx < n and 0 <= ny < m and room[nx][ny] != 1:
        clean_room(nx, ny, z)  # 후진


clean_room(r, c, d)
print(clean_square)
