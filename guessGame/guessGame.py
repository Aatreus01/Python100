#TODO
# create a guess mechanic with counter function
# help the user to find the answer by declaring if the guess is too high or too low
# create an easy and hard mode
import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
number = random.randint(0, 100)
guessCounter = 5
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if (difficulty == "easy"): guessCounter = 10 
while (guessCounter != 0):
    print(f"You have {guessCounter} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if(guess > number):
        print("Too high.")
    elif(guess == number):
        print(f"You got it! The answer was {number}")
        break
    else:
        print("Too low.")
    print("Guess again.")
    guessCounter -= 1
