def group(lst):
    result = {}
    groups_iter = -1
    
    if len(lst) == 0:
        return result

    previous_elem = None

    for i in range(0,len(lst)):
        if previous_elem != lst[i]:
            previous_elem = lst[i]
            groups_iter += 1
            result[groups_iter] = [lst[i]]
        else:
            result[groups_iter].append(lst[i])
    
    return result.values()

if __name__ == '__main__':
    print(group([1, 1, 1, 2, 3, 1, 1]))
    print(group([1, 2, 1, 2, 3, 3]))