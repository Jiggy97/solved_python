# n은 보석의 개수, k는 가방의 개수
n, k = map(int, input().split())

jewelry = []
for i in range(n):
    # m은 보석의 무게, v는 보석의 가갹
    m, v = map(int, input().split())
    jewelry.append((m, v))

bag = []
for i in range(k):
    bag.append(int(input()))

jewelry.sort(key=lambda x: (x[1], x[0]), reverse=True)
bag.sort()

result = 0
for i in jewelry:
    for j in bag:
        if i[0] <= j:
            result += i[1]
            idx = bag.index(j)
            del bag[idx]
            break

print(result)
