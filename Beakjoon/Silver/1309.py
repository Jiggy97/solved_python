N = int(input())

dp = [1,1]

for i in range(1, N):
    dp[0] = dp[0] + 2 * dp[1]
    dp[1] = dp[0] - dp[1]
    # print(dp)

print((dp[0] + 2 * dp[1]) % 9901)