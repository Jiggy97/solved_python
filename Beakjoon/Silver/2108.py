from collections import Counter

n = int(input())
n_list = []
for i in range(n):
    n_list.append(int(input()))

counts = Counter(n_list)
mode = max(counts, key=counts.get)
print(round(sum(n_list) / n))
n_list.sort()
print(n_list[int(n/2)])
print(mode)
print(max(n_list) - min(n_list))
