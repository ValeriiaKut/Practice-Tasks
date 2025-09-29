def maximum(x, y, a, b):
    if x == y == a == b:
        print("The biggest number is", x)
    else:
        print("The biggest number is", max(x, y, a, b))


try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))
    number4 = int(input("Enter the fourth number: "))
    maximum(number1, number2, number3, number4)
except ValueError:
    print("Please enter a number")
