def fibonacci(n):
    result = []
    fib1 = 1
    fib2 = 1
    fib = fib1 + fib2

    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        result.append(fib1)
        result.append(fib2)
        result.append(fib)
        while n > 3:
            fib1 = fib2
            fib2 = fib
            fib = fib1 + fib2
            result.append(fib)
            n -= 1
    return result

if __name__ == '__main__':
    print(fibonacci(10))
