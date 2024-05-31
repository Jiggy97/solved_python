# n = int(input())
# A = [(i + 1) for i in range(n)]
# B = []
# C = []
#
#
# def hanoi_top(a, b):
#     if len(B) == n:
#         return
#
#     print(a, end=' ')
#     print(b)
#     hanoi_top()
#
#
# if n % 2 == 0:
#     hanoi_top(1, 2)
# else:
#     hanoi_top(1, 3)
#

def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi_tower(n - 1, start, 6 - start - end)
    print(start, end)
    hanoi_tower(n - 1, 6 - start - end, end)


n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3)
