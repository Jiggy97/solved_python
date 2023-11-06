n = int(input())
plus = []
minus = []
result = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else:
        result += num

plus.sort()
minus.sort()

for i in range(len(plus)-1, -1, -2):
    if i == 0:
        result += plus[i]
    else:
        result += plus[i] * plus[i - 1]

for j in range(0, len(minus), 2):
    if j == len(minus) - 1:
        result += minus[j]
    else:
        result += minus[j] * minus[j + 1]

print(result)
