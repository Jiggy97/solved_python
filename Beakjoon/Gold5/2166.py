def polygon_area(vertices):
    n = len(vertices)
    area = 0

    # Sum up the determinant
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # Next vertex (wrapping around using modulo)
        area += x1 * y2 - x2 * y1

    return abs(area) / 2


# 입력 받기
n = int(input())
vertices = [tuple(map(int, input().split())) for _ in range(n)]

# 면적 계산
area = polygon_area(vertices)
print(f"{area:.1f}")
