import sys
sys.setrecursionlimit(10**6)

n = int(input())
tower_list = list(map(int, input().split()))
reception = [0] * n
stack = []


def stack_pop(array, st, index):
    if st[-1] < array[index]:
        ix = st.pop(-1)
        reception[ix] = index
        if len(stack) != 0:
            stack_pop(array, st, index)


for i in range(n - 1, 0, -1):
    stack.append(i)
    if tower_list[i] < tower_list[i - 1]:
        idx = stack.pop(-1)
        reception[idx] = i
        if len(stack) != 0:
            stack_pop(tower_list, stack, i)

for r in reception:
    print(r, end=' ')
