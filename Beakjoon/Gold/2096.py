n = int(input())
num_list = []

for i in range(n):
    a, b, c = map(int, input().split())
    if i == 0:
        num_list = [(a, a), (b, b), (c, c)]
        continue

    min0, max0 = num_list[0]
    min1, max1 = num_list[1]
    min2, max2 = num_list[2]

    min_tmp = a + min(min0, min1)
    max_tmp = a + max(max0, max1)
    num_list[0] = (min_tmp, max_tmp)

    min_tmp = b + min(min0, min1, min2)
    max_tmp = b + max(max0, max1, max2)
    num_list[1] = (min_tmp, max_tmp)

    min_tmp = c + min(min1, min2)
    max_tmp = c + max(max1, max2)
    num_list[2] = (min_tmp, max_tmp)

min_result, max_result = int(1e9), 0
for i in range(3):
    min_tmp, max_tmp = num_list[i]
    min_result = min(min_result, min_tmp)
    max_result = max(max_result, max_tmp)

print(max_result, min_result)

'''
# 메모리 초과난 풀이
for _ in range(n):
    num_list.append(list(map(int, input().split())))

min_dp = [[0] * 3 for _ in range(n)]
max_dp = [[0] * 3 for _ in range(n)]
for i in range(3):
    min_dp[0][i], max_dp[0][i] = num_list[0][i], num_list[0][i]

for i in range(1, n):
    min_dp[i][0] = min(min_dp[i - 1][0] + num_list[i][0], min_dp[i - 1][1] + num_list[i][0])
    min_dp[i][1] = min(min_dp[i - 1][0] + num_list[i][1],
                       min_dp[i - 1][1] + num_list[i][1], min_dp[i - 1][2] + num_list[i][1])
    min_dp[i][2] = min(min_dp[i - 1][1] + num_list[i][2], min_dp[i - 1][2] + num_list[i][2])

    max_dp[i][0] = max(max_dp[i - 1][0] + num_list[i][0], max_dp[i - 1][1] + num_list[i][0])
    max_dp[i][1] = max(max_dp[i - 1][0] + num_list[i][1],
                       max_dp[i - 1][1] + num_list[i][1], max_dp[i - 1][2] + num_list[i][1])
    max_dp[i][2] = max(max_dp[i - 1][1] + num_list[i][2], max_dp[i - 1][2] + num_list[i][2])

print(max(max_dp[-1]), end=' ')
print(min(min_dp[-1]))
'''
