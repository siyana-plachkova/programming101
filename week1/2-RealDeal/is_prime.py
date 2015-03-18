from sum_of_divisors import sum_of_divisors

def is_prime(n):
    
    if n < 0:
        n = abs(n)

    return sum_of_divisors(n) == n + 1

if __name__ == '__main__':
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(8))
    print(is_prime(11))
    print(is_prime(-10))