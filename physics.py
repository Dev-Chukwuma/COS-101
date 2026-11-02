def calculate_speed(distance, time):
    if time == 0:
        raise ValueError("Time cannot be zero.")
    return distance / time


def calculate_force(mass, acceleration):
    return mass * acceleration


def calculate_weight(mass, gravity):
    return mass * gravity


def calculate_density(mass, volume):
    if volume == 0:
        raise ValueError("Volume cannot be zero.")
    return mass / volume


def calculate_work_done(force, distance):
    return force * distance


print("1. Calculate Speed")
print("2. Calculate Force")
print("3. Calculate Weight")
print("4. Calculate Density")
print("5. Calculate Work Done")

choice = input("Choose a formula (1-5): ")

if choice == "1":
    distance = float(input("Enter distance in metres: "))
    time = float(input("Enter time in seconds: "))
    print("Speed:", calculate_speed(distance, time), "m/s")

elif choice == "2":
    mass = float(input("Enter mass in kilograms: "))
    acceleration = float(input("Enter acceleration in m/s²: "))
    print("Force:", calculate_force(mass, acceleration), "N")

elif choice == "3":
    mass = float(input("Enter mass in kilograms: "))
    gravity = float(input("Enter gravitational acceleration in m/s²: "))
    print("Weight:", calculate_weight(mass, gravity), "N")

elif choice == "4":
    mass = float(input("Enter mass in kilograms: "))
    volume = float(input("Enter volume in m³: "))
    print("Density:", calculate_density(mass, volume), "kg/m³")

elif choice == "5":
    force = float(input("Enter force in newtons: "))
    distance = float(input("Enter distance in metres: "))
    print("Work Done:", calculate_work_done(force, distance), "J")

else:
    print("Invalid choice. Please select a number from 1 to 5.")
