def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


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


while True:
    print("\n1. Calculate Speed")
    print("2. Calculate Force")
    print("3. Calculate Weight")
    print("4. Calculate Density")
    print("5. Calculate Work Done")
    print("0. Exit")

    choice = input("Choose a formula (0-5): ")

    if choice == "0":
        print("Goodbye!")
        break

    elif choice == "1":
        distance = get_number("Enter distance in metres: ")
        time = get_number("Enter time in seconds: ")
        try:
            print("Speed:", calculate_speed(distance, time), "m/s")
        except ValueError as error:
            print(error)

    elif choice == "2":
        mass = get_number("Enter mass in kilograms: ")
        acceleration = get_number("Enter acceleration in m/s²: ")
        print("Force:", calculate_force(mass, acceleration), "N")

    elif choice == "3":
        mass = get_number("Enter mass in kilograms: ")
        gravity = get_number("Enter gravitational acceleration in m/s²: ")
        print("Weight:", calculate_weight(mass, gravity), "N")

    elif choice == "4":
        mass = get_number("Enter mass in kilograms: ")
        volume = get_number("Enter volume in m³: ")
        try:
            print("Density:", calculate_density(mass, volume), "kg/m³")
        except ValueError as error:
            print(error)

    elif choice == "5":
        force = get_number("Enter force in newtons: ")
        distance = get_number("Enter distance in metres: ")
        print("Work Done:", calculate_work_done(force, distance), "J")

    else:
        print("Invalid choice. Please select a number from 0 to 5.")
