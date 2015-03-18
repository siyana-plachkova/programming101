def palindrome(obj):
    obj = str(obj)
    return obj == obj[::-1]

if __name__ == '__main__':
    print(palindrome(123))
    print(palindrome('kapak'))
    print(palindrome(12321))