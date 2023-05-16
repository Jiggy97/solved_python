N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A는 오름차순, B는 내림차순으로 정렬
A.sort()

result = 0
for a in A:
    result += a * max(B)
    B.pop(B.index(max(B)))

print(result)
