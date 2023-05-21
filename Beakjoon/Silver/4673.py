def d(n):
    next_num = n
    while n > 0:
        next_num += n % 10
        n //= 10
    return next_num


def solution():
    numbers = set(range(1, 10001))
    self_numbers = set()

    for num in numbers:
        next_num = d(num)
        while next_num <= 10000:
            self_numbers.add(next_num)
            next_num = d(next_num)

    result = numbers - self_numbers
    return sorted(result)

# 결과 출력
answer = solution()
for num in answer:
    print(num)
