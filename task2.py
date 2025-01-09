"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random
def game():
    number = random.randint(1,10)
    for i in range(4):
        guess = int(input(f"Enter your #{i+1} guess: "))
        if guess == number:
            print(f"You got it! The number was {number}")
            break
        else:
            print("Incorrect. Try again.")
    print(f"You couldn't guess it, the number was {number}")
    
def title():
    print("Welcome to the number guessing game!")
    print("A random integer will be chosen between 1 and 10")
    print("You will have 4 guesses to choose the right number.")
    print("Good Luck!")
     
title()
p_ready = input("Are you ready to play? (yes/no): ")
if p_ready == 'yes' or 'Yes' or 'YES' or 'y':
    game()

    
