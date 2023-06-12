import sys
import heapq

input = sys.stdin.readline

n = int(input())
card_bundle = []

for _ in range(n):
    heapq.heappush(card_bundle, int(input()))

result = 0
if len(card_bundle) == 1:
    print(result)
else:
    for i in range(n-1):
        first = heapq.heappop(card_bundle)
        second = heapq.heappop(card_bundle)

        result += first + second
        heapq.heappush(card_bundle, first + second)

    print(result)
