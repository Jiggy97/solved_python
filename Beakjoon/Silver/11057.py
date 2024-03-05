# DP 
# 규칙 찾는게 중요

n = int(input())
dp = [1] * 10
for i in range(n-1):
    for j in range(1, 10):
        dp[j] += dp[j-1]

# print(dp)
print(sum(dp) % 10007)
