def calculator(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operator"

# User input for operator and operands
operator = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(calculator(operator, num1, num2))
