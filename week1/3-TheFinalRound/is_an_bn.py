def is_an_bn(word):
    word_half = len(word)//2
    count_as=0
    count_bs=0

    if word_half == 0:
        return True

    for ch in range(0, word_half):
        if word[ch] != 'a':
            return False
        count_as += 1

    for ch in range(word_half, len(word)):
        if word[ch] != 'b':
            return False
        count_bs += 1

    return count_as == count_bs

if __name__ == '__main__':
    print(is_an_bn(""))
    print(is_an_bn("rado"))
    print(is_an_bn("aaabb"))
    print(is_an_bn("aaabbb"))
    print(is_an_bn("aabbaabb"))
    print(is_an_bn("bbbaaa"))
    print(is_an_bn("aaaaabbbbb"))