def trap(height):
    if not height:
        return 0

    n = len(height)
    left_max = [0] * n
    right_max = [0] * n

    # 왼쪽에서부터의 최대 높이 계산
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    # 오른쪽에서부터의 최대 높이 계산
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    # 고이는 물의 양 계산
    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - height[i]

    return trapped_water


# 입력값 처리 및 함수 호출
H, W = map(int, input().split())
heights = list(map(int, input().split()))

result = trap(heights)
print(result)
