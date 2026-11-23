
numbers = [
    12, 15, 18, 20, 15,
    22, 25, 18, 30, 15,
    35, 40, 22, 18, 45,
    50, 15, 30, 18, 55
]

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

numbers.sort()

length = len(numbers)

if length % 2 == 1:
    middle = numbers[length // 2]
else:
    middle = (numbers[length // 2 - 1] + numbers[length // 2]) / 2

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

highest_frequency = max(frequency.values())

most_common = []

for num, count in frequency.items():
    if count == highest_frequency:
        most_common.append(num)

print("Numbers:", numbers)
print("Sum:", total)
print("Mean:", average)
print("Median:", middle)
print("Mode:", most_common)
