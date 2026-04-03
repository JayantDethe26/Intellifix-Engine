def read_numbers(file_path):
try:
with open(file_path, "r") as f:
lines = f.readlines()
numbers = []
for line in lines:
stripped_line = line.strip()
if stripped_line:  # Check if line is not empty
try:
numbers.append(int(stripped_line))
except ValueError:
print(f"Warning: Skipping invalid number {stripped_line}")
return numbers
except FileNotFoundError:
raise

def write_numbers(file_path, numbers):
with open(file_path, "w") as f:
for num in numbers:
f.write(str(num) + "\n")