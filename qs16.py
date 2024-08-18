def write_details(file_path, employees):
    with open(file_path, 'w') as file:
        for employee in employees:
            file.write(f"Name: {employee['name']}, Age: {employee['age']}, Salary: {employee['salary']}\n") # Check format


if __name__ == "__main__":
    employees = [
        {"name": "SD", "age": 30, "salary": 50000},
        {"name": "Rick", "age": 25, "salary": 60000},
        {"name": "Soumyadeep", "age": 35, "salary": 70000}
    ]
    
    write_details("employees.txt", employees)
    print("Employee details have been written to employees.txt")