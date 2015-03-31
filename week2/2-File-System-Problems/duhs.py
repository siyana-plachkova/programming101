import os
import sys


def du(path):
    size_bytes = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.isfile(filepath):
                size_bytes += os.path.getsize(filepath)

        for dirname in dirnames:
            dirpath = os.path.join(dirpath, dirname)
            if os.path.isdir(dirpath):
                size_bytes += du(dirpath)

    return size_bytes


def duhs():
    path = sys.argv[1]

    if not os.path.isdir(path):
        return "The given path is not a directory."

    size_bytes = du(path)

    output_string = '{} size is:'.format(path)
    if size_bytes == 0:
        return '%s 0 B' % output_string

    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

    i = 0
    while size_bytes >= 1024 and i < len(suffixes) - 1:
        size_bytes /= 1024.
        i += 1

    new_size = ('%.2f' % size_bytes).rstrip('0').rstrip('.')
    return '%s %s %s' % (output_string, new_size, suffixes[i])


if __name__ == '__main__':
    print(duhs())
