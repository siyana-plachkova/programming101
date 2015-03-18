def to_number(digits):
    number = ""

    for digit in digits:
        number += str(digit)

    return int(number)

if __name__ == '__main__':
    print(to_number([1,2,3]))
    print(to_number([9,9,9,9,9]))
    print(to_number([1,2,3,0,2,3]))