import random

number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

while True:
    try:
       guess = int(input("Enter your guess: "))
       attempts += 1
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} correctly!")
        print(f"Total attemps: {attempts}")
        break