import sys
from random import randint

def generate_numbers():
    filename = sys.argv[1]
    file = open(filename, "w+")
    for files in range(int(sys.argv[2]) - 1):
        number = randint(1, 1000)
        file.write(str(number) + " ")
    file.write(str(randint(1, 1000)))

if __name__ == '__main__':
    print(generate_numbers())