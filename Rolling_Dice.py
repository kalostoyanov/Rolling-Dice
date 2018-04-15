import random

min = int(input("Please enter the minimum number: "))
max = int(input("Please enter the maximum number: "))

number_to_guess = random.randrange(min,max)

guess_number = int(input("Please try to guess the number: "))
while guess_number != number_to_guess:
    print(f"{guess_number} is not correct!")
    if guess_number < number_to_guess:
        print("Try something higher.")
    else:
        print("Try something lower.")
    guess_number = int(input("Please try again: "))
print("This is correct!!!")