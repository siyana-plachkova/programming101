def char_histogram(string):
    histogram = {}
    for ch in string:
        if not ch in histogram.keys():
            histogram[ch] = string.count(ch)

    return histogram

if __name__ == '__main__':
    print(char_histogram("Python!"))
    print(char_histogram("AAAAaaa!!!"))