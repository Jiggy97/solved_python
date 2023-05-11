n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))

rope.sort()
weight = []

for i in range(n):
    weight.append((n - i) * rope[i])

print(max(weight))

