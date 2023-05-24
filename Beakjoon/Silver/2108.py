from collections import Counter
import sys

n = int(sys.stdin.readline())
n_list = []
for i in range(n):
    n_list.append(int(sys.stdin.readline()))

n_list.sort()

mean = round(sum(n_list) / n)

median = n_list[int(n/2)]

# 제출했을 때 틀렸다고 뜨는 코드
# 이유 > 문제를 잘 읽어보면 두 번째로 작은 최빈값을 출력하라고 돼있음,,ㅅㅂㅅㅂ
# counts = Counter(n_list)
# mode_value = max(counts, key=counts.get)

counts = Counter(n_list).most_common()
mode = 0
if len(counts) == 1:
    mode = counts[0][0]
elif counts[0][1] == counts[1][1]:
    mode = counts[1][0]
else:
    mode = counts[0][0]

range_n = max(n_list) - min(n_list)

print(mean)
print(median)
print(mode)
print(range_n)
