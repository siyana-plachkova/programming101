def iterations_of_nan_expand(expanded):
    not_a_count = expanded.count("Not a")

    if not_a_count == 0 and len(expanded) != 0:
        return False

    return not_a_count

if __name__ == '__main__':
    print(iterations_of_nan_expand(""))
    print(iterations_of_nan_expand("Not a NaN"))
    print(iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
    print(iterations_of_nan_expand("Show these people!"))