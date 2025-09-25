def classification(num):
    if num <= 10:
        print("your number is less than or equal to 10")
    elif 10 < num <= 25:
        print("your number is between 10 and 25 or equal to 25")
    else:
        print("your number is greater than 25")


try:
    number = int(input("Enter a number: "))
    classification(number)
except ValueError:
    print("Please enter a number")
