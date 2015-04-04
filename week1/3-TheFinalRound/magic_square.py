def row_sum(matrix, i_ind):
    r_sum = 0
    for ind in range(0, len(matrix)):
        r_sum += matrix[i_ind][ind]
    return r_sum


def col_sum(matrix, j_ind):
    c_sum = 0
    for ind in range(0, len(matrix)):
        c_sum += matrix[ind][j_ind]
    return c_sum


def sec_diagonal_sum(matrix):
    diagonal_sum = 0
    for ind in range(0, len(matrix)):
        diagonal_sum += matrix[ind][len(matrix) - 1 - ind]
    return diagonal_sum


def main_diagonal_sum(matrix):
    diagonal_sum = 0
    for ind in range(0, len(matrix)):
        diagonal_sum += matrix[ind][ind]
    return diagonal_sum


def magic_square(matrix):
    all_sum_list = []
    for index in range(0, len(matrix)):
        all_sum_list.append(row_sum(matrix, index))
        all_sum_list.append(col_sum(matrix, index))

    all_sum_list.append(main_diagonal_sum(matrix))
    all_sum_list.append(sec_diagonal_sum(matrix))

    return all_sum_list.count(all_sum_list[0]) == len(all_sum_list)

if __name__ == '__main__':
    print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
    print(magic_square([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
    print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
    print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
