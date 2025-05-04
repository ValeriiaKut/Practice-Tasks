def light_distance():
    try:
        speed_of_light = 299792458
        second = 1
        minute = 60 * second
        hour = 60 * minute
        day = 24 * hour
        year = 365 * day
        speed_of_light_per_year = speed_of_light * year
        speed_of_light_kilometer = speed_of_light_per_year / 1000
        print(
            f"The distance in kilometers that light travels in one year is {speed_of_light_kilometer:.2f} km.")
        years = float(input("Enter the number of years: "))
        print(
            f"The distance in kilometers that light travels in {years} years is {years * speed_of_light_kilometer} km.")

    except ValueError:
        print("Please enter a number.")


light_distance()
