def to_binary(n):
    if n == 0:
        return [0]

    result = []
    while n > 0:
        result.append(n % 2)
        n //= 2
    return result[::-1]


def next_hack(n):
    flag = False

    while not flag:
        n += 1
        binary_number = to_binary(n)

        if binary_number == binary_number[::-1] and binary_number.count(1) % 2 == 1:
            flag = True

    return n


if __name__ == '__main__':
    print(next_hack(0))
    print(next_hack(10))
    print(next_hack(8031))
