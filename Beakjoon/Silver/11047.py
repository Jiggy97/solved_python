n, k = map(int, input().split())
coin_val = []
for _ in range(n):
    coin_val.append(int(input()))

coin_cnt = 0
for i in range(n-1, -1, -1):
    if k >= coin_val[i]:
        coin_cnt += k // coin_val[i]
        k -= coin_val[i] * (k // coin_val[i])

print(coin_cnt)
