from collections import deque


def AC(function, num, array):
    queue = deque(array)
    flag = 0

    if num == 0:
        queue = []

    for j in function:
        if j == 'R':
            flag += 1
            continue

        if j == 'D':
            if len(queue) == 0:
                return "error"
            if flag % 2 == 0:
                queue.popleft()
            else:
                queue.pop()

    else:
        if flag % 2 == 0:
            return "[" + ",".join(queue) + "]"
        else:
            queue.reverse()
            return "[" + ",".join(queue) + "]"


T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = input()[1:-1].split(',')

    print(AC(p, n, arr))
