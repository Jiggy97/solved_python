import heapq


def dijkstra(start):
    heap = []
    dist[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        w, v = heapq.heappop(heap)

        if dist[v] < w:
            continue

        for i in graph[v]:
            cost = dist[v] + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

dist = [float('inf')] * (V + 1)
dijkstra(K)

for j in range(1, V + 1):
    if dist[j] == float('inf'):
        print('INF')
        continue
    print(dist[j])
