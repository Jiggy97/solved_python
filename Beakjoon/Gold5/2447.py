n = int(input())


def star(n):
    if n == 1:
        return "*"

    arr = star(n//3)
    tmp = []
    # print(arr)
    for i in range(len(arr)):
        tmp.append(arr[i]*3)
    for j in range(len(arr)):
        tmp.append(arr[j] + ' '*(n//3) + arr[j])
    for k in range(len(arr)):
        tmp.append(arr[k]*3)
    return tmp


result = star(n)
for line in result:
    print(line)
