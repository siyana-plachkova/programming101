def sum_of_divisors(n):
    if n == 1:
        return 1

    divisors_sum = n + 1
    for num in range(2, n//2 + 1):
        if n % num == 0:
            divisors_sum += num
    return divisors_sum

if __name__ == '__main__':
    print(sum_of_divisors(8))
    print(sum_of_divisors(7))
    print(sum_of_divisors(1))
    print(sum_of_divisors(1000))
