from file_utils import read_numbers

def divide_numbers(a, b):
if b == 0:
raise ValueError("Cannot divide by zero")
return a / b

def process():
try:
numbers = read_numbers("data.txt")
total = 0
for num in numbers:
try:
total += divide_numbers(100, num)
except ValueError as e:
print(f"Error processing number {num}: {e}")
print("Total:", total)
except FileNotFoundError:
print("Error: File 'data.txt' not found")
except Exception as e:
print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
process()