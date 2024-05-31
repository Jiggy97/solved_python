# n, k = map(int, input().split())
#
# # 물건 정보 저장
# things = []
#
# for _ in range(n):
#     w, v = map(int, input().split())
#     things.append((w, v))
#
# # 특정 물건이 들어갔을 때, 가치
# cases = [[] for _ in range(n)]
#
# # 가치의 값이 높은 순으로 정렬
# things = sorted(things, key=lambda x: x[1], reverse=True)
# # 가치가 가장 높은 순서로 경우의 수 추출
# for i in range(n):
#     j = i + 1
#     weight, value = things[i][0], things[i][1]
#     while j < n:
#         if weight + things[j][0] == k:
#             cases[i].append(value + things[j][1])
#             weight, value = things[i][0], things[i][1]
#             j += 1
#             continue
#         elif weight + things[j][0] > k:
#             j += 1
#             continue
#         weight += things[j][0]
#         value += things[j][1]
#         j += 1
#     cases[i].append(value)
#
# result = []
# for i in range(n):
#     result.append(max(cases[i]))
# print(max(result))


n, k = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(n)]

# dp 테이블 초기화
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for w in range(1, k+1):
        weight = things[i-1][0]
        value = things[i-1][1]

        if weight <= w:
            # i번째 물건을 배낭에 추가하는 경우와 추가하지 않는 경우 중 더 큰 값 선택
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
        else:
            dp[i][w] = dp[i-1][w]

print(dp[n][k])
