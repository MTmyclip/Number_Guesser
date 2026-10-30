import random

number = random.randint(1, 10)
guess = int(input("Guess a number from 1 to 10: "))

while guess != number:
    hint = "higher" if guess < number else "lower"
    guess = int(input("Nope, go " + hint + ": "))

print("You got it! The number was", number)
