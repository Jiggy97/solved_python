n = int(input())
home = []
for _ in range(n):
    home.append(list(map(int, input().split())))
count = 0


def check(direction, row, col):
    if direction == 0:
        col += 1

    if direction == 1:
        row += 1

    if direction == 2:
        col, row = col + 1, row + 1

    if row == n - 1 and col == n - 1:
        return True


def move(direction, row, col):
    move_list = []

    if direction == 0:
        if col + 2 < n and home[row][col + 2] == 0:
            move_list.append((0, row, col + 1))
        if (row + 1 < n and col + 2 < n and home[row][col + 2] == 0
                and home[row + 1][col + 1] == 0 and home[row + 1][col + 2] == 0):
            move_list.append((2, row, col + 1))

    if direction == 1:
        if row + 2 < n and home[row + 2][col] == 0:
            move_list.append((1, row + 1, col))
        if (row + 2 < n and col + 1 < n and home[row + 2][col] == 0\
                and home[row + 1][col + 1] == 0 and home[row + 2][col + 1] == 0):
            move_list.append((2, row + 1, col))

    if direction == 2:
        if row + 1 < n and col + 2 < n and home[row + 1][col + 2] == 0:
            move_list.append((0, row + 1, col + 1))
        if row + 2 < n and col + 1 < n and home[row + 2][col + 1] == 0:
            move_list.append((1, row + 1, col + 1))
        if (row + 2 < n and col + 2 < n and home[row + 1][col + 2] == 0
                and home[row + 2][col + 1] == 0 and home[row + 2][col + 2] == 0):
            move_list.append((2, row + 1, col + 1))

    return move_list


def dfs(d, r, c):
    global count

    if check(d, r, c):
        count += 1
        return

    for i, j, k in move(d, r, c):
        dfs(i, j, k)


dfs(0, 0, 0)
print(count)
