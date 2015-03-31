import sys

def sum_numbers():
    filename = sys.argv[1]
    file = open(filename, "r")
    content = file.read()
    num_list = content.split(" ")
    ints_sum = 0
    
    for num in num_list:
        ints_sum += int(num)
    
    return ints_sum
    
if __name__ == '__main__':
    print(sum_numbers())