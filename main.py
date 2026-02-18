"""
Making a number guessing game with rounds, 
"""
#imported a random number to generate a random number
import random

#function for getting an  integer from the user
def get_valid_int(prompt):
    while True:
         try:
            return int(input(prompt).strip())
         except ValueError:
             print("Please enter a valid integer.")

#function to get a valid yes/no response
def get_valid_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice == "y" or choice == "n":
            return (choice)
        else:
            print("Please enter 'y' for yes or 'n' for no.")

#A FUNCTION THAT PLAYS one RoUND only
def play_game():
    #ask them to select a number range
    low = get_valid_int("Enter the lowest number of the range: ")
    high = get_valid_int("Enter the highest number of the range: ")


#gonna ask for attempts
max_attempts = get_valid_int("How many attempts do you want? ")

#generate a random number
secret_number = random.randint(low, high)
#the number of attempts used
attempts_used = 0


#the game loop
while attempts_used < max_attempts:
    guess = get_valid_int("Enter your guess: ")
    attempts_used += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempts_used} attempts.")
    
#if user runs out of attempts
print(f"Sorry, you've run out of attempts. The number was {secret_number}.")
