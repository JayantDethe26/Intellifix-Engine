def read_numbers(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    numbers = []
    for line in lines:
        numbers.append(int(line.strip()))

    return numbers


def write_numbers(file_path, numbers):
    with open(file_path, "w") as f:
        for num in numbers:
            f.write(str(num) + "\n")
