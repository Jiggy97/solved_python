import sys
sys.setrecursionlimit(10 ** 5)

n, m = map(int, input().split())

relation = [[] for _ in range(n)]
visited = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)


def dfs(rel, v, now, c):
    global ans
    v[now] = 1

    for i in rel[now]:
        if v[i] == 0:
            if c == 3:
                ans = 1
                return 1
            v[i] = 1
            dfs(rel, v, i, c + 1)

    v[now] = False


for j in range(n):
    ans = 0
    dfs(relation, visited, j, 0)
    if ans == 1:
        print(1)
        break

else:
    print(0)
