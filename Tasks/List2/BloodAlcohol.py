def blood_alcohol(a):
    if 0.2 >= a >= 0:
        print("You are sober")
    elif 1 >= a > 0.2:
        print("You are after drinking/light intoxication")
    else:
        print("You are intoxicated!")


try:
    number = float(input("Print your blood alcohol concentration: "))
    blood_alcohol(number)
except ValueError:
    print("Print the number ")
