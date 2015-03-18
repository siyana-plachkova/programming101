def count_consonants(str):
    consonants = "bcdfghjklmnpqrstvwxz"
    consonants_count = 0

    for ch in str.lower():
        if ch in consonants:
            consonants_count += 1

    return consonants_count

if __name__ == '__main__':
    print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))