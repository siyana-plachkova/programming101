from count_words import count_words


def unique_words_count(arr):
    return len(count_words(arr))

if __name__ == '__main__':
    print(unique_words_count(["apple", "banana", "apple", "pie"]))
    print(unique_words_count(["python", "python", "python", "ruby"]))
    print(unique_words_count(["HELLO!"] * 10))
