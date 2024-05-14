n = int(input())
solutions = list(map(int, input().split()))
'''
# 첫 풀이, 시간 초과
near_zeros = []
index = []
for i in range((n // 2) + 1):
    near_zero = 100000
    jdx = 0
    for j in range(n):
        if i == j:
            continue
        val = solutions[i] + solutions[j]
        if abs(val) < abs(near_zero):
            near_zero = val
            jdx = j
    near_zeros.append((abs(near_zero), i, jdx))

near_zeros.sort()
print(solutions[near_zeros[0][1]], end=' ')
print(solutions[near_zeros[0][2]])
'''

solutions.sort()
left = 0
right = n - 1
near_zero = 2000000000
min_val, max_val = 0, 0

while left < right:
    val = solutions[left] + solutions[right]
    if abs(val) < abs(near_zero):
        min_val, max_val = solutions[left], solutions[right]
        near_zero = val
    if val < 0:
        left += 1
    else:
        right -= 1

print(min_val, end=' ')
print(max_val)
