# n, m = map(int, input().split())
#
# set_list = [[] for _ in range(n + 1)]
#
# for _ in range(m):
#     cal, a, b = map(int, input().split())
#     if cal == 0:
#         set_list[a].append(b)
#         set_list[b].append(a)
#     if cal == 1:
#         if a == b:
#             print('YES')
#         if b in set_list[a] or a in set_list[b]:
#             print('YES')
#         else:
#             print('NO')

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


import sys
input = sys.stdin.read
data = input().split()

n, m = int(data[0]), int(data[1])
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

index = 2
results = []
for _ in range(m):
    cal, a, b = int(data[index]), int(data[index+1]), int(data[index+2])
    index += 3
    if cal == 0:
        union(a, b)
    elif cal == 1:
        if find(a) == find(b):
            results.append('YES')
        else:
            results.append('NO')

print("\n".join(results))
