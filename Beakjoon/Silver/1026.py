n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B_1 = sorted(B, reverse=True)
indexes = []
for i in B_1:
    indexes.append(B.index(i))

A_tmp = sorted(A)
for i in range(n):
    A[indexes[i]] = A_tmp[i]

S = 0
for i in range(n):
    S += A[i] * B[i]

print(S)
