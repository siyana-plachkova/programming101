def sum_matrix(m):
    result = 0
    for lst in m:
        for elem in lst:
            result += elem
    return result

if __name__ == '__main__':
    print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
