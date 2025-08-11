# Basic Calculator Program
# This program performs basic arithmetic operations based on user input

def calculator():
    print("Welcome to the Basic Calculator!")
    
    # Get user input for two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return
    
    # Get user input for the operation
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform the calculation based on the operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Error: Invalid operation. Please use +, -, *, or /.")
        return
    
    # Display the result
    print(f"\nResult: {num1} {operation} {num2} = {result}")

# Run the calculator function
if __name__ == "__main__":
    calculator()