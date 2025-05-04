def average_speed(t, t1, dist, dist1):
    average_distance = dist + dist1
    average_time = (t/60) + (t1/60)
    speed = average_distance/average_time
    print(f"Your average speed is {speed} kilometers per minutes")


try:
    time = float(input("Enter your time in minutes of the first distance: "))
    distance = float(input("Enter first distance in kilometers: "))
    distance1 = float(input("Enter second distance in kilometers: "))
    time1 = float(input("Enter your time in minutes of the second distance: "))

    if time <= 0 or time1 <= 0 or distance <= 0 or distance1 <= 0:
        raise ValueError("All input values must be positive numbers.")

    print(f"Your time and distance of the first road: {time} minutes, {distance} kilometers.")
    print(f"Your time and distance of the second road: {time1} minutes, {distance1} kilometers.")
    average_speed(time, time1, distance, distance1)
except ValueError as e:
    print(f"Invalid input {e}")
