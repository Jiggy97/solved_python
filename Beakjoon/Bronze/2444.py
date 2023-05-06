n = int(input())

# 윗 부분 출력
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))

# 아래 부분 출력
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "*" * (2*i-1))
