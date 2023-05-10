n = int(input())

p = list(map(int, input().split()))
p.sort()

time = 0
tmp = 0

for i in p:
    tmp += i
    time += tmp

print(time)
