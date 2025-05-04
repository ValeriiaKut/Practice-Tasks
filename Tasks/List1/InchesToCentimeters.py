def inches_to_centimeters(inches):
    centimeters = inches * 2.54
    print(f"The result is:  {centimeters} centimeters.")


try:
    number = float(input("Enter a number of inches: "))
    inches_to_centimeters(number)
except ValueError:
    print("Enter a valid number")
