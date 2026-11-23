
numbers = [
    12, 15, 18, 20, 15,
    22, 25, 18, 30, 15,
    35, 40, 22, 18, 45,
    50, 15, 30, 18, 55
]


def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_mean(numbers):
    return calculate_sum(numbers) / len(numbers)


def calculate_median_mode(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length % 2 == 1:
        median = sorted_numbers[length // 2]
    else:
        median = (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2

    frequency = {}

    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    highest_frequency = max(frequency.values())

    mode = []

    for num, count in frequency.items():
        if count == highest_frequency:
            mode.append(num)

    return median, mode


print("Numbers:", numbers)
print("Sum:", calculate_sum(numbers))
print("Mean:", calculate_mean(numbers))

median, mode = calculate_median_mode(numbers)

print("Median:", median)
print("Mode:", mode)

