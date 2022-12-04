"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        if len(numbers)%2 == 1:
            medianVal = numbers[int((len(numbers) - 1) / 2)]
        else:
            temp1 = numbers[int((len(numbers) - 2) / 2)]
            temp2 = numbers[int(len(numbers) / 2)]
            medianVal = (temp1 + temp2) / 2
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(medianVal)
