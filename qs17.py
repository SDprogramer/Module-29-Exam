def read_employees(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")


if __name__ == "__main__":
    file_path = "employees.txt"
    read_employees(file_path)
