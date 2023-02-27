name = "Paulina"
greeting = "Hello SheGoesTech"
print(name)
print(greeting)
print(greeting[:5] + f", {name}, welcome to" + greeting[5:] + "!")

x = 3
y = 5
if (x == y):
    print("The items are the same.")
else:
    print("The items are different.")

personAge = int(input("Please enter your age:"))
personName = input("Please enter your name:")
ageLimit = 18
if (personAge >= ageLimit):
    print(f"Welcome to the club, {personName}!")
else:
    yearsToWait = ageLimit - personAge
    print(f"Sorry, {personName}, come back in {yearsToWait} years!")