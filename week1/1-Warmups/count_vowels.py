def count_vowels(str):
    vowels = "aeiouy"
    vowels_count = 0
    for ch in str.lower():
        if ch in vowels:
            vowels_count += 1
    return vowels_count

if __name__ == '__main__':
    print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
