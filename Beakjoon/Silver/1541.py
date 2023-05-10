Str = input()

cal = Str.split('-')

Sum = sum(map(int, cal[0].split('+')))
for i in cal[1:]:
    Sum -= sum(map(int, i.split('+')))

print(Sum)
