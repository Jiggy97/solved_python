n = int(input())
meeting_list = []

for _ in range(n):
    start, end = map(int, input().split())
    meeting_list.append((start, end))

meeting_list.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0
for i in meeting_list:
    if end_time <= i[0]:
        count += 1
        end_time = i[1]

print(count)
