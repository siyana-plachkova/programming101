def nan_expand(times):
    if times == 0:
        return ""

    return " ".join(["Not a"] * times) + " NaN"

if __name__ == '__main__':
    print(nan_expand(0))
    print(nan_expand(1))
    print(nan_expand(2))
    print(nan_expand(3))