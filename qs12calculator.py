def addition(num1, num2): 
    return num1 + num2

def subtraction(num1, num2): 
    return num1 - num2

def multiplication(num1, num2): 
    return num1 * num2

def division(num1, num2): 
    if num2 != 0:
        return num1 / num2
    else:
        print("Invalid input")


print(addition(4, 5))
print(division(6, 3))
print(division(6, 0))