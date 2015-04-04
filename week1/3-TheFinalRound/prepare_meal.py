def prepare_meal(number):
    max = 0
    for num in range(number, 0, -1):
        if number % (3 ** num) == 0:
            max = num
            break

    if number == 5:
        return "eggs"
    if max == 0:
        return ""

    eggs = ""
    if number % 5 == 0:
        eggs = " and eggs"

    return " ".join(["spam"] * max) + eggs

if __name__ == '__main__':
    print(prepare_meal(3))
    print(prepare_meal(27))
    print(prepare_meal(7))
    print(prepare_meal(5))
    print(prepare_meal(15))
    print(prepare_meal(45))
