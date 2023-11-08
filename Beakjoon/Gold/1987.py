dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []


def can_move(x, y, visited, alphabet_set):
    return 0 <= x < r and 0 <= y < c and not visited[x][y] and board[x][y] not in alphabet_set


def dfs(x, y, count, alphabet_set):
    global max_count
    visited[x][y] = True
    alphabet_set.add(board[x][y])
    max_count = max(max_count, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if can_move(nx, ny, visited, alphabet_set):
            dfs(nx, ny, count + 1, alphabet_set)

    visited[x][y] = False
    alphabet_set.remove(board[x][y])


r, c = map(int, input().split())
board = [list(map(str, input())) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
alphabet_set = set()
max_count = 0

dfs(0, 0, 1, alphabet_set)
print(max_count)
