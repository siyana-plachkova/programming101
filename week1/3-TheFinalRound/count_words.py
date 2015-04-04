def count_words(arr):
    result = {}
    for word in arr:
        if word not in result.keys():
            result[word] = arr.count(word)
    return result

if __name__ == '__main__':
    print(count_words(["apple", "banana", "apple", "pie"]))
    print(count_words(["python", "python", "python", "ruby"]))
