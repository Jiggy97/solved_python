n = int(input())
word_list = []
alphabet = {}
for _ in range(n):
    word = input()
    for w in word:
        if w in alphabet:
            continue
        else:
            alphabet[w] = 0
    word_list.append(word)

sorted_len = sorted(word_list, key=len, reverse=True)
result = 0
value = 9
for word in sorted_len:
    string = ''
    for w in word:
        if alphabet[w] != 0:
            string += str(alphabet[w])
        else:
            alphabet[w] = value
            string += str(value)
            value -= 1
    result += int(string)

print(result)

# alphabet = {}
# for _ in range(n):
#     word = input()
#     for w in word:
#         if w in alphabet:
#             alphabet[w] += 1
#         else:
#             alphabet[w] = 1
#     word_list.append(word)
#
# alphabet_desc = dict(sorted(alphabet.items(), key=lambda item: item[1], reverse=True))
# print(alphabet_desc)
#
# value = 9
# for ap in alphabet_desc:
#     alphabet[ap] = 9
#     value -= 1
#
# result = 0
# for word in word_list:
#     string = ''
#     for w in word:
#         string += str(alphabet[w])
#     result += int(string)
#
# print(result)
