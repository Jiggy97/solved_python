from collections import deque


# 내 풀이
# def bfs(graph, number, start):
#     visited = [False] * (number + 1)
#     visited[start] = True
#     queue = deque([start])
#     count = 0
#     while queue:
#         x = queue.popleft()
#
#         for com1, com2 in graph:
#             if x == com1 and not visited[com2]:
#                 queue.append(com2)
#                 visited[com2] = True
#                 count += 1
#             if x == com2 and not visited[com1]:
#                 queue.append(com1)
#                 visited[com1] = True
#                 count += 1
#
#     return count
#
#
# n = int(input())
# k = int(input())
# networkInfo = []
#
# for i in range(k):
#     c1, c2 = map(int, input().split())
#     networkInfo.append((c1, c2))
#
# result = bfs(networkInfo, n, 1)
# print(result)


def bfs(graph, computer_num, start):
    visited = [False] * len(graph)
    visited[start] = True
    queue = deque([start])
    count = 0

    while queue:
        x = queue.popleft()

        for computer in graph[x]:
            if not visited[computer]:
                queue.append(computer)
                visited[computer] = True
                count += 1

    return count


n = int(input())
k = int(input())
network = [[] for _ in range(n + 1)]

for _ in range(k):
    c1, c2 = map(int, input().split())
    network[c1].append(c2)
    network[c2].append(c1)

result = bfs(network, n, 1)
print(result)
