def dfs(graph, start, visited, count):
    count += 1
    row, col = start
    visited[row][col] = True
    for j in graph[row][col]:
        if not visited[row][col]:



r, c = map(int, input().split())
board = [[] for _ in range(r)]
visit = [[False] * c for _ in range(r)]
print(board)
for i in range(r):
    alphabet = input()
    for ch in alphabet:
        board[i].append(ch)

result = 0
dfs(board, (0, 0), visit, result)
print(result)
