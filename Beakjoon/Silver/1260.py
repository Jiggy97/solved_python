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
            # 현재 탐색한 노드 i[0] 방문 여부를 따져야 할 노드는 i[0]과 간선으로 연결 되어 있는 i[1]
            # 방문하지 않았을 경우 i[1]노드 큐에 입력 후 방문처리
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
        # 현재 탐색한 노드 i[0] 방문 여부를 따져야 할 노드는 i[0]과 간선으로 연결 되어 있는 i[1]
        # 방문하지 않았을 경우 i[1]노드를 기준으로 다시 탐색
        if not visited[i[1]]:
            dfs(graph, i[1], visited)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 양방향으로 간선 그래프에 입력
    graph[a].append((a, b))
    graph[b].append((b, a))

# 오름 차순으로 그래프 정렬
for line in graph:
    line.sort(key=lambda x: (x[1], x[0]))

dfs_vis = [False] * (n + 1)
dfs(graph, v, dfs_vis)
print()
bfs_vis = [False] * (n + 1)
bfs(graph, v, bfs_vis)
