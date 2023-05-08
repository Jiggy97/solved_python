n, m = map(int, input().split())
basket = [x for x in range(1, n + 1)]
for _ in range(m):
    i, j, k = map(int, input().split())
    tmp1 = basket[k-1:j]
    tmp2 = basket[i-1:k-1]
    basket = basket[0:i-1] + tmp1 + tmp2 + basket[j:n]

for i in basket:
    print(i, end=" ")
