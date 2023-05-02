a, b = map(int, input().split())

reversed_a = int(str(a)[::-1])
reversed_b = int(str(b)[::-1])

if reversed_b > reversed_a:
    print(reversed_b)
else: print(reversed_a)
