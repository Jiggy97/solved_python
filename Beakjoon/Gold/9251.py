import sys

str1 = input()
str2 = input()
dp = [[0] * len(str1) for _ in range(len(str2))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str[2]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
