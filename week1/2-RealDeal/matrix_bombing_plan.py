def matrix_bombing_plan(matrix):
    output = {}
    n = len(matrix)
    m = len(matrix[0])

    for i in range(0, n):
        for j in range(0, m):
            matrix_sum = 0

            for temp_i in range(0, n):
                for temp_j in range(0, m):
                    bombed_el = matrix[temp_i][temp_j] - matrix[i][j]
                    bombed_el = 0 if bombed_el < 0 else bombed_el

                    if i == temp_i + 1 and j == temp_j + 1 or i == temp_i + 1 and j == temp_j or i == temp_i and j == temp_j + 1:
                        matrix_sum += bombed_el
                    elif i == temp_i - 1 and j == temp_j - 1 or i == temp_i - 1 and j == temp_j or i == temp_i and j == temp_j - 1:
                        matrix_sum += bombed_el
                    elif i == temp_i - 1 and j == temp_j + 1 or i == temp_i + 1 and j == temp_j - 1:
                        matrix_sum += bombed_el
                    else:
                        matrix_sum += matrix[temp_i][temp_j]

            output[(i, j)] = matrix_sum

    return output

if __name__ == '__main__':
    print(matrix_bombing_plan([[1,2,3], [4,5,6], [7,8,9]]))