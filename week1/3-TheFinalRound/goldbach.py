def sum_of_divisors(n):
    if n == 1:
        return 1

    divisors_sum = n + 1
    for num in range(2, n//2 + 1):
        if n % num == 0:
            divisors_sum += num
    return divisors_sum


def is_prime(n):
    if n < 0:
        n = abs(n)

    return sum_of_divisors(n) == n + 1


def goldbach(n):
    result = []
    first_num = 2

    while first_num <= n // 2:
        if is_prime(first_num) and is_prime(n - first_num):
            result.append((first_num, n - first_num))
        first_num += 1

    return sorted(result, key=lambda el: el[0])

if __name__ == '__main__':
    print(goldbach(4))
    print(goldbach(6))
    print(goldbach(8))
    print(goldbach(10))
    print(goldbach(100))
