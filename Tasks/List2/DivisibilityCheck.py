def divisible(num1, num2):
    if num2 != 0:
        if num1 % num2 == 0:
            print("Number 1 is divisible by number 2")
        else:
            print("Number 1 is not divisible by number 2")
    else:
        print("Error: Division by zero is not allowed.")


print("Welcome to DivisibilityCheck ")
try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    divisible(number1, number2)
except ValueError:
    print("Please enter only numbers.")

