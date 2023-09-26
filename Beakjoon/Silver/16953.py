a, b = map(int, input().split())
count = 1

while a < b:
    count += 1
    if b % 2 == 0:
        b /= 2
    else:
        if b % 10 != 1:
            break
        if b < 10:
            break
        b //= 10

if a == b:
    print(count)
else:
    print(-1)
