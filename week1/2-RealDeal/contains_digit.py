def contains_digit(number, digit):
    return str(number).count(str(digit)) != 0

if __name__ == '__main__':
    print(contains_digit(123, 4))
    print(contains_digit(42, 2))
    print(contains_digit(1000, 0))
    print(contains_digit(12346789, 5))
