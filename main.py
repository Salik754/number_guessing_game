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
def play_game