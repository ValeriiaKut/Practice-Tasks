def maximum(a, b, c):
    if a > b and a > c:
        print(f"{a} is the maximum")
    elif b > a and b > c:
        print(f"{b} is the maximum")
    elif c > a and c > b:
        print(f"{c} is the maximum")
    elif a == b and b > c:
        print(f"{a} is the maximum")
    elif c == a and a > b:
        print(f"{c} is the maximum")
    elif b == c and b > a:
        print(f"{b} is the maximum")
    else:
        print("the numbers are equal")


try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))
    maximum(number1, number2, number3)
except ValueError:
    print("Please enter a number")