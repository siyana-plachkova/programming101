def sum_of_digits(n):
    if n < 0:
        n = abs(n)
    digits_sum = 0
    while n > 0:
        digits_sum += n % 10
        n //= 10
    return digits_sum

if __name__ == '__main__':
    print(sum_of_digits(-1325132435356))
