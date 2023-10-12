def isGroup(word):
    wordArray = list(word)
    for w in wordArray:
        idx = []
        for j in range(len(word)):
            if w == word[j]:
                idx.append(j)
        if len(idx) == 1: continue
        for k in range(len(idx) - 1):
            if (idx[k + 1] - idx[k]) != 1: return False

    return True


n = int(input())
count = 0
for i in range(n):
    word = input()
    if isGroup(word):
        count += 1

print(count)
