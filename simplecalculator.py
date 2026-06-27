def calculator (num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return num1 // num2
    else:
        print("Error: Invalid operation. Please use +, -, *, or /.")
        return None

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
result = calculator(num1, num2, operation)
print(result)
