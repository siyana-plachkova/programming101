def reduce_file_path(path):
    dir_list = path.split("/")
    reduced = list(filter(lambda elem: elem != "" and elem != ".", dir_list))
    path_reduced = []

    for ind in range(0, len(reduced)):
        if reduced[ind] != "..":
            path_reduced.append(reduced[ind])
        elif len(path_reduced) != 0:
            path_reduced.pop()

    return "/" + ("/".join(path_reduced))


if __name__ == '__main__':
    print(reduce_file_path("/"))
    print(reduce_file_path("/srv/../"))
    print(reduce_file_path("/srv/www/htdocs/wtf/"))
    print(reduce_file_path("/srv/www/htdocs/wtf"))
    print(reduce_file_path("/srv/./././././"))
    print(reduce_file_path("/etc//wtf/"))
    print(reduce_file_path("/etc/../etc/../etc/../"))
    print(reduce_file_path("//////////////"))
    print(reduce_file_path("/../"))
