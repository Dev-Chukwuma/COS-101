
from statistics import median, multimode

print("LIST STATISTICS PROGRAM")

user_input = input("Enter numbers separated by commas: ")

try:
    numbers = [float(num.strip()) for num in user_input.split(",")]

    if not numbers:
        raise ValueError

    
    total = sum(numbers)
    average = total / len(numbers)
    middle = median(numbers)
    most_common = multimode(numbers)

    
    print("\n========== RESULTS ==========")
    print("Numbers:", numbers)
    print("Sum:", total)
    print("Average (Mean):", average)
    print("Median:", middle)
    print("Mode:", most_common)
    print("=============================")

except ValueError:
    print("Invalid input! Please enter valid numbers separated by commas.")
  
