n = int(input())

if n == 1:
    print(0)
    exit()

if n <= 3:
    print(1)
    exit()

dp = [0] * (n + 1)
dp[2], dp[3] = 1, 1
dp[4] = 2

for i in range(5, n + 1):
    divide2 = i / 2
    divide3 = i / 3

    if i % 6 == 0:
        dp[i] = min(dp[i-1], dp[i // 2], dp[i // 3]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i-1], dp[i // 2]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i-1], dp[i // 3]) + 1
    else:
        dp[i] = dp[i-1] + 1

print(dp[n])
