from is_prime import is_prime

def prime_number_of_divisors(n):
    divisor = 1
    count_divisors = 0
    while divisor <= n:
        if n % divisor == 0:
            count_divisors += 1
        divisor += 1
    return is_prime(count_divisors)

if __name__ == '__main__':
    print(prime_number_of_divisors(7))
    print(prime_number_of_divisors(8))
    print(prime_number_of_divisors(9))