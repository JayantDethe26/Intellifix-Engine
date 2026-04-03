from math_utils import divide_numbers
from file_utils import read_numbers

def process():
    numbers = read_numbers("data.txt")

    total = 0
    for num in numbers:
        total += divide_numbers(100, num)

    print("Total:", total)

if __name__ == "__main__":
    process()
