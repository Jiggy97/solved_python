def stringToArr(string_arr):
    arr = []
    for char in string_arr:
        if char == '[' or char == ']' or char == ',':
           continue
        arr.append(int(char))

    return arr


def AC(function, num, string):
    array = stringToArr(string)
    for idx in range(len(function)):
        if array is None:
            return "error"

        if function[idx] == 'R':
            if function[idx + 1] == 'R':
                function = function[:idx] + function[idx + 2:]
            else:
                array = array[::-1]

        if function[idx] == 'D':
            array.pop(0)

    return array


T = int(input())
for i in range(T):
    p = input()
    n = int(input())
    st = input()
    print(AC(p, n, st))
