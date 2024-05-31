T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    c = y - x
    val = 0
    idx = 0
    count = 0

    while val < c:
        count += 1
        if count % 2 != 0:
            idx += 1
        val += idx

    print(count)
