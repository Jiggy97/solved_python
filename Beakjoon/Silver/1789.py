import sys

s = int(sys.stdin.readline())

num = 0
n = 0
while num <= s:
    n += 1
    num += n
    if num == s:
        n += 1
        break

print(n - 1)
