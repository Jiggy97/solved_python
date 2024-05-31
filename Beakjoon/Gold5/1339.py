n = int(input())
word_list = []
alphabet = {}

for _ in range(n):
    word_list.append(input())
for i in word_list:
    for j in range(len(i)):
        digit = len(i) - j - 1
        if i[j] not in alphabet:
            alphabet[i[j]] = 10 ** digit
            continue
        alphabet[i[j]] += 10 ** digit

alpha_info = list(alphabet.values())
alpha_info.sort(reverse=True)
ans = 0
idx = 0
for i in range(9, 9-len(alpha_info), -1):
    ans += alpha_info[idx] * i
    idx += 1
print(ans)
