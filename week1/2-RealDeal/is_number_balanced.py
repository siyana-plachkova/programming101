def is_number_balanced(n):
    first_half_digits_sum = 0
    second_half_digits_sum = 0
    count_digits = len(str(n))

    if count_digits == 1:
        return True

    if count_digits % 2 == 0:
        for digit in str(n)[:count_digits//2]:
            first_half_digits_sum += int(digit)
        for digit in str(n)[count_digits//2:]:
            second_half_digits_sum += int(digit)
    else:
        for digit in str(n)[:count_digits//2]:
            first_half_digits_sum += int(digit)
        for digit in str(n)[count_digits//2 + 1:]:
            second_half_digits_sum += int(digit)

    return first_half_digits_sum == second_half_digits_sum

if __name__ == '__main__':
    print(is_number_balanced(9))
    print(is_number_balanced(11))
    print(is_number_balanced(13))
    print(is_number_balanced(121))
    print(is_number_balanced(4518))
    print(is_number_balanced(28471))
    print(is_number_balanced(1238033))
