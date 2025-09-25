def sign_and_parity(num):
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")

    if num > 0:
        print(num, "is positive")
    elif num < 0:
        print(num, "is negative")
    else:
        print(num, "is zero")

try:
    numer = int(input("Enter a number: "))
    sign_and_parity(numer)
except ValueError:
    print("Please enter a number")