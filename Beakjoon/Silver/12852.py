n = int(input())

dp = [[0, 0] for _ in range(n + 1)]
dp[2][0] = 1
dp[3][0] = 1
dp[4][0] = 2

for i in range(4, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        select = [dp[i - 1][0], dp[i // 2][0], dp[i // 3][0]]
        dp[i][0] = min(select) + 1
        dp[i][1] = select.index(min(select))
    elif i % 2 == 0:
        select = [dp[i - 1][0], dp[i // 2][0]]
        dp[i][0] = min(select) + 1
        dp[i][1] = select.index(min(select))
    elif i % 3 == 0:
        select = [dp[i - 1][0], dp[i // 3][0]]
        dp[i][0] = min(select) + 1
        if select.index(min(select)) == 0:
            dp[i][1] = select.index(min(select))
        else:
            dp[i][1] = select.index(min(select)) + 1
    else:
        dp[i][0] = dp[i - 1][0] + 1
        dp[i][1] = 0

print(dp[n][0])
while n != 1:
    print(n, end=" ")
    if dp[n][1] == 0:
        n -= 1
    elif dp[n][1] == 1:
        n //= 2
    else:
        n //= 3
print(n)
