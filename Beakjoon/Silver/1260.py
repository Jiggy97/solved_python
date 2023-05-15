from collections import deque


# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현제 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i[1]]:
                queue.append(i[1])
                visited[i[1]] = True


# DFS 메서드 정의
def dfs(graph, start, visited):
    # 현재 노드를 방문 처리
    visited[start] = True
    print(start, end=' ')
    # 현재 노드와 다른 노드를 재귀적으로 방문
    for i in graph[start]:
        if not visited[i[1]]:
            dfs(graph, i[1], visited)


n, m, v = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append((a, b))
    g[b].append((b, a))

for line in g:
    line.sort(key=lambda x: (x[1], x[0]))

dfs_vis = [False] * (n + 1)
dfs(g, v, dfs_vis)
print()
bfs_vis = [False] * (n + 1)
bfs(g, v, bfs_vis)
