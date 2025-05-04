def seconds_calculations():
    second = 1
    minute = 60 * second
    hour = 60 * minute
    day = 24 * hour
    week = 7 * day
    year = 365 * day
    print(f"Seconds in 1 minute {minute}")
    print(f"Seconds in 1 hour {hour}")
    print(f"Seconds in 1 day {day}")
    print(f"Seconds in 1 week {week}")
    print(f"Seconds in 1 year {year}")
    age = float(input("Enter your age: "))
    print(f"You lived {age * year} seconds!")


seconds_calculations()
