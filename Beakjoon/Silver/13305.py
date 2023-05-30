n = int(input())

city_dis = list(map(int, input().split(" ")))

oil_price = list(map(int, input().split(" ")))

oil_price.pop()
min_oil = min(oil_price)
total_dis = sum(city_dis)
result = 0
for i in range(n-1):
    if oil_price[i] == min_oil:
        result += total_dis * min_oil
        break
    else:
        result += city_dis[i] * oil_price[i]
        total_dis -= city_dis[i]

print(result)
