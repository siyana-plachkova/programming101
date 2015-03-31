import sys

def read_files():
    result = ""
    if len(sys.argv) > 1:
        #print(sys.argv)
        for file in range(1, len(sys.argv)):
            #print(sys.argv[file])
            filename = sys.argv[file]
            text_file = open(filename, "r")
            text = text_file.read()
            result += text + "\n"
    return result


if __name__ == '__main__':
    print(read_files())