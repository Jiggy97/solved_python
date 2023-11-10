dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []


def can_move(x, y, alphabet_set):
    return 0 <= x < r and 0 <= y < c and board[x][y] not in alphabet_set


def dfs(x, y, count, alphabet_set):
    global max_count
    alphabet_set.add(board[x][y])
    max_count = max(max_count, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if can_move(nx, ny, alphabet_set):
            dfs(nx, ny, count + 1, alphabet_set)

    alphabet_set.remove(board[x][y])


r, c = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(r)]
max_count = 0

dfs(0, 0, 1, set())
print(max_count)
