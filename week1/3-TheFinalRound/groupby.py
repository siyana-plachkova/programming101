def groupby(func, seq):
    result = {}

    for elem in seq:
        func_output = func(elem)

        if not func_output in result.keys():
            result[func_output] = [elem]
        else:
            result[func_output].append(elem)

    return result

if __name__ == '__main__':
    print(groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))
    print(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
    print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))