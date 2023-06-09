import sys

input = sys.stdin.readline


# 다른 사람의 풀이
for _ in range(int(input())):
    recruit = [list(map(int, input().split())) for _ in range(int(input()))]
    recruit_asc = sorted(recruit)

    top = 0
    result = 1
    for i in range(1, len(recruit_asc)):
        if recruit_asc[i][1] < recruit_asc[top][1]:
            result += 1
            top = i

    print(result)

# 내 풀이
# 시간 초과
# for _ in range(int(input())):
#     result = 0
#     n = int(input())
#     recruit = [list(map(int, input().split())) for _ in range(n)]
#
#     for i in recruit:
#         for j in recruit:
#             if i[0] > j[0] and i[1] > j[1]:
#                 result += 1
#                 break
#
#     print(n - result)

