from collections import deque

t = int(input())


def bfs():
    ans = False
    queue = deque([])
    queue.append((home_x, home_y))
    visited = set()
    visited.add((home_x, home_y))

    while queue:
        x, y = queue.popleft()
        if abs(x - pen_x) + abs(y - pen_y) <= 1000:
            ans = True
            break
        else:
            for c_x, c_y in con_list:
                if (c_x, c_y) in visited:
                    continue
                if abs(x - c_x) + abs(y - c_y) <= 1000:
                    queue.append((c_x, c_y))
                    visited.add((c_x, c_y))
    return ans


for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    con_list = []
    for _ in range(n):
        a, b = (map(int, input().split()))
        con_list.append((a, b))
    pen_x, pen_y = map(int, input().split())

    if bfs():
        print("happy")
    else:
        print("sad")
