def zero_insert(n):
    result = []
    n_str = str(n)
    for i in range(0, len(n_str) - 1):
        if n_str[i] == n_str[i+1] or (int(n_str[i]) + int(n_str[i+1])) % 10 == 0:
            result.append(n_str[i] + '0')
        else:
            result.append(n_str[i])
    result.append(n_str[len(n_str)-1])

    return int(''.join(result))

if __name__ == '__main__':
    print(zero_insert(116457))