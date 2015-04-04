from palindrome import palindrome


def p_score(n):
    if palindrome(n):
        return 1
    return 1 + p_score(n + int(str(n)[::-1]))

if __name__ == '__main__':
    print(p_score(121))
    print(p_score(48))
    print(p_score(198))
