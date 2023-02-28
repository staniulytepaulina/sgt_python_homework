# Task 4 - Find all numbers until 100 that are divisible by 7.
numbers = [*range(0, 100)]
divisibleNumbers = []
for number in numbers:
    if number % 7 == 0:
        divisibleNumbers.append(number)
print(divisibleNumbers)

# Task 5 - Reverse the string
word = str(input("Please enter any word: "))
reversedWord = ""
for character in word:
    reversedWord = character + reversedWord
print(reversedWord)


# Task 6 - Return factorial of the number

def factorial(provided_number):
    factorial_number = 1
    for integer in range(1, provided_number + 1):
        factorial_number = factorial_number * integer
    return factorial_number


factorialNumber = input("Provide the number you want to get the factorial number of: ")
try:
    value = int(factorialNumber)
    print(factorial(value))
except ValueError:
    print("Provided value can't be converted to integer.")
