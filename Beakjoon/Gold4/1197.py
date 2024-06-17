# 백준 1197번 문제: 최소 스패닝 트리 (MST)
# 크루스칼 알고리즘 사용

# 유니온 파인드 (Union-Find) 자료구조 정의
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(edges, V):
    # 간선을 가중치의 오름차순으로 정렬
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(V)
    mst_weight = 0
    mst_edges = 0

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += weight
            mst_edges += 1
            if mst_edges == V - 1:
                break

    return mst_weight


V, E = map(int, input().split())
edges = []

for _ in range(E):
    edges.append(list(map(int, input().split())))

result = kruskal(edges, V)
print(result)
