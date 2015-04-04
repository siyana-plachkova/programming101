def is_increasing(seq):
    for i in range(len(seq) - 1):
        if seq[i] >= seq[i+1]:
            return False
    return True

if __name__ == '__main__':
    print(is_increasing([1, 2, 3, 4, 5]))
    print(is_increasing([1]))
    print(is_increasing([5, 6, -10]))
    print(is_increasing([1, 1, 1, 1, 1]))
