n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [100000] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        count = dp[i - coin] + 1
        if count < dp[i]:
            dp[i] = count

if dp[k] == 100000:
    print(-1)
else:
    print(dp[k])
