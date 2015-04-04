from factorial import factorial


def fact_digits(n):
    if n < 0:
        n = abs(n)
    digits_sum = 0
    while n > 0:
        digits_sum += factorial(n % 10)
        n //= 10
    return digits_sum

if __name__ == '__main__':
    print(fact_digits(999))
