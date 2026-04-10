from utils import read_numbers, divide_numbers

def process():
numbers = read_numbers("data.txt")

total = 0
for num in numbers:
try:
total += divide_numbers(100, num)
except ZeroDivisionError:
print(f"Cannot divide 100 by {num}. Skipping...")
except ValueError:
print(f"Invalid number: {num}. Skipping...")

print("Total:", total)

if __name__ == "__main__":
process()