n = int(input())
arr_list = []

for _ in range(n):
    a, b = map(int, input().split())
    arr_list.append((a, b))

rankings = [1] * n

for i in range(n):
        for j in range(n):
            if arr_list[i][0] < arr_list[j][0] and arr_list[i][1] < arr_list[j][1]:
                rankings[i] += 1

for r in range(n):
    if r == n-1:
        print(rankings[r])
        break
    print(rankings[r], end=' ')
