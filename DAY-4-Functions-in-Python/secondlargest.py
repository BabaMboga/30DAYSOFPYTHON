numbers = [34,984,26465,234,2,94753,378643,3763]

def second_largest(numbers):
    numbers.sort()
    second_number = numbers[-2]
    print(f"The second largest number is: {second_number}")

second_largest(numbers)