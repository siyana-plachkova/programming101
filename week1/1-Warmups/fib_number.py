from to_number import to_number
from fibonacci import fibonacci

def fib_number(n):
    return to_number(fibonacci(n))

if __name__ == '__main__':
    print(fib_number(3))
    print(fib_number(10))