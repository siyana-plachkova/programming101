def factorial(n):
    fact = 1
    if (n == 0) or (n == 1):
        return 1

    while n > 0:
        fact *= n
        n -= 1
    return fact

if __name__ == '__main__':
    print(factorial(5))
