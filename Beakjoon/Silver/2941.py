words = input()
croatia = ['c=', 'c-', 'd-', 'dz=', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    words = words.replace(i, '*')

print(len(words))
