import sys
import heapq

input = sys.stdin.readline

# n은 보석의 개수, k는 가방의 개수
n, k = map(int, input().split())

jewelries = []
for _ in range(n):
    # m은 보석의 무게, v는 보석의 가갹
    m, v = map(int, input().split())
    heapq.heappush(jewelries, (-v, m))

bags = []
for _ in range(k):
    heapq.heappush(bags, int(input()))

result = 0
while bags:
    jewelry = heapq.heappop(jewelries)
    while True:
        if jewelry[1] <= bags[0]:
            result += -jewelry[0]
            heapq.heappop(bags)
            break

print(result)
