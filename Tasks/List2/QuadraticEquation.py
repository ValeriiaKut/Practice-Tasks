import math


def quadratic_equation(a, b, c):
    if a != 0:
        equation1 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
        equation2 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
        print("Your coefficients: ", equation1, equation2)
    else:
        print("Your equation is not quadratic ")


try:
    number_a = float(input("Print A number: "))
    number_b = float(input("Print B number: "))
    number_c = float(input("Print C number: "))
    quadratic_equation(number_a, number_b, number_c)
except ValueError:
    print("Please, print the number.")
