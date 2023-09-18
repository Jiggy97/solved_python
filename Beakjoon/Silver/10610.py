n = input()

if "0" not in n or int(n) % 3 != 0:
    print("-1")
else:
    print("".join(sorted(map(str, n), reverse=True)))
