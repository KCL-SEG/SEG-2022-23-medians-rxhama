"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

if len(numbers)%2 == 1:
    medianVal = numbers[(len(numbers) - 1) / 2]
else:
    temp1 = numbers[(len(numbers) - 2) / 2]
    temp2 = numbers[len(numbers) / 2]
    medianVal = (temp1 + temp2) / 2
