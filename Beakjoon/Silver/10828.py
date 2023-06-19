import sys
n = int(sys.stdin.readline())  # input 으로 하면 시간 초과

stack = []

for _ in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        stack.append(s[1])
    elif s[0] == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(stack))
    elif s[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
