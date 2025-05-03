def calculate(a, b):
    try:
        summa = a + b
        difference = a - b
        product = a * b
        quotient = a / b
        remainder = a % b
        print(f"The summa is {summa}."
              f"The difference is {difference}."
              f"The product is {product}."
              f"The quotient is {quotient}."
              f"The remainder is {remainder}.")
    except ZeroDivisionError:
        print("Second number is 0.")


try:
    number1 = int(input("Enter the first number : "))
    number2 = int(input("Enter the second number : "))
    print(f"Your numbers are: {number1} , {number2}")
    calculate(number1, number2)
except ValueError:
    print("Enter a valid number")
