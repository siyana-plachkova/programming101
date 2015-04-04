def sum_of_digits(n):
    if n < 0:
        n = abs(n)
    digits_sum = 0
    while n > 0:
        digits_sum += n % 10
        n //= 10
    return digits_sum


def is_credit_card_valid(number):
    num_str = str(number)

    if len(num_str) % 2 == 0:
        return False

    num_transformed = num_str[::-1]
    concat_new = ""

    for ind in range(0, len(num_transformed)):
        if ind % 2 != 0:
            concat_new += str(int(num_transformed[ind]) * 2)
        else:
            concat_new += num_transformed[ind]

    sum_transformed_digits = sum_of_digits(int(concat_new))

    return sum_transformed_digits % 10 == 0

if __name__ == '__main__':
    print(is_credit_card_valid(79927398713))
    print(is_credit_card_valid(79927398715))
