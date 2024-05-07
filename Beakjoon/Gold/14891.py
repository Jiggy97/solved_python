from collections import deque

one_queue = deque(list(map(int, input())))
two_queue = deque(list(map(int, input())))
three_queue = deque(list(map(int, input())))
four_queue = deque(list(map(int, input())))

k = int(input())
spin_list = []
for i in range(k):
    spin_list.append((map(int, input().split())))


def one(direction):
    if direction == -1:
        if one_queue[2] != two_queue[6]:
            if two_queue[2] != three_queue[6]:
                if three_queue[2] != four_queue[6]:
                    four_queue.insert(0, four_queue.pop())
                three_queue.append(three_queue.popleft())
            two_queue.insert(0, two_queue.pop())
        one_queue.append(one_queue.popleft())
    elif direction == 1:
        if one_queue[2] != two_queue[6]:
            if two_queue[2] != three_queue[6]:
                if three_queue[2] != four_queue[6]:
                    four_queue.append(four_queue.popleft())
                three_queue.insert(0, three_queue.pop())
            two_queue.append(two_queue.popleft())
        one_queue.insert(0, one_queue.pop())


def two(direction):
    if direction == -1:
        if one_queue[2] != two_queue[6]:
            one_queue.insert(0, one_queue.pop())
        if two_queue[2] != three_queue[6]:
            if three_queue[2] != four_queue[6]:
                four_queue.append(four_queue.popleft())
            three_queue.insert(0, three_queue.pop())
        two_queue.append(two_queue.popleft())
    elif direction == 1:
        if one_queue[2] != two_queue[6]:
            one_queue.append(one_queue.popleft())
        if two_queue[2] != three_queue[6]:
            if three_queue[2] != four_queue[6]:
                four_queue.insert(0, four_queue.pop())
            three_queue.append(three_queue.popleft())
        two_queue.insert(0, two_queue.pop())


def three(direction):
    if direction == -1:
        if three_queue[2] != four_queue[6]:
            four_queue.insert(0, four_queue.pop())
        if two_queue[2] != three_queue[6]:
            if two_queue[6] != one_queue[2]:
                one_queue.append(one_queue.popleft())
            two_queue.insert(0, two_queue.pop())
        three_queue.append(three_queue.popleft())
    elif direction == 1:
        if three_queue[2] != four_queue[6]:
            four_queue.append(four_queue.popleft())
        if two_queue[2] != three_queue[6]:
            if two_queue[6] != one_queue[2]:
                one_queue.insert(0, one_queue.pop())
            two_queue.append(two_queue.popleft())
        three_queue.insert(0, three_queue.pop())


def four(direction):
    if direction == -1:
        if three_queue[2] != four_queue[6]:
            if two_queue[2] != three_queue[6]:
                if one_queue[2] != two_queue[6]:
                    one_queue.insert(0, one_queue.pop())
                two_queue.append(two_queue.popleft())
            three_queue.insert(0, three_queue.pop())
        four_queue.append(four_queue.popleft())
    elif direction == 1:
        if three_queue[2] != four_queue[6]:
            if two_queue[2] != three_queue[6]:
                if one_queue[2] != two_queue[6]:
                    one_queue.append(one_queue.popleft())
                two_queue.insert(0, two_queue.pop())
            three_queue.append(three_queue.popleft())
        four_queue.insert(0, four_queue.pop())


for n, d in spin_list:
    if n == 1:
        one(d)
    if n == 2:
        two(d)
    if n == 3:
        three(d)
    if n == 4:
        four(d)

point = 0
if 1 == one_queue[0]:
    point += 1
if 1 == two_queue[0]:
    point += 2
if 1 == three_queue[0]:
    point += 4
if 1 == four_queue[0]:
    point += 8

print(point)
