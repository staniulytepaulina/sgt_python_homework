# Task 7

def max_number(num1, num2, num3):
    highest_number = 0
    numbers = [num1, num2, num3]
    for number in numbers:
        if number > highest_number:
            highest_number = number
    print(highest_number)
    return highest_number


max_number(3, 5, 9)


# Task 8

def reverse_string(string):
    reversed_string = ""
    character_index = len(string) - 1
    while character_index >= 0:
        reversed_string = reversed_string + string[character_index]
        character_index = character_index - 1
    print(reversed_string)
    return reversed_string


reverse_string("hello")


# Task 9

def sum_numbers(*num: tuple) -> float:
    """Takes in a list of numbers and returns the sum of them."""
    sum_number = 0
    for i in num:
        sum_number += i
    print(sum_number)
    return sum_number


sum_numbers(8, 20, 2)
