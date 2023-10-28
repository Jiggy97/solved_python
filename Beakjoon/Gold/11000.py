import heapq

n = int(input())
class_info = []
for _ in range(n):
    s, t = map(int, input().split())
    class_info.append((s, t))

class_sort = sorted(class_info, key=lambda x: x[0])
end_list = list()
heapq.heappush(end_list, class_sort[0][1])

for i in range(1, n):
    if class_sort[i][0] >= end_list[0]:
        heapq.heappop(end_list)
    heapq.heappush(end_list, class_sort[i][1])

print(len(end_list))
