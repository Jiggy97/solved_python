L, C = map(int, input().split())
candidates = list(map(str, input().split()))
candidates.sort()
password = ''


def back(idx, pw):
    if len(pw) == L:
        count1, count2 = 0, 0
        for ch in pw:
            if ch in ['a', 'e', 'i', 'o', 'u']:
                count1 += 1
            else:
                count2 += 1
        if count1 >= 1 and count2 >= 2:
            print(pw)
        return

    for i in range(idx, C):
        if candidates[i] not in pw:
            pw += candidates[i]
            back(i + 1, pw)
            pw = pw[:-1]


back(0, password)
