import random

# Function to safely get an integer from the user
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")

# Function to get a valid y/n response
def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice == "y" or choice == "n":
            return choice
        else:
            print("Please enter 'y' or 'n' only.")

# Function that plays one round of the game
def play_game():
    # Ask for number range
    low = get_valid_int("Enter the lowest number: ")
    high = get_valid_int("Enter the highest number: ")

    # Ensure range is valid
    while high <= low:
        print("High number must be greater than low number.")
        high = get_valid_int("Enter the highest number: ")

    # Ask for attempts
    max_attempts = get_valid_int("How many attempts do you want? ")

    # Generate random number
    secret_number = random.randint(low, high)

    attempts_used = 0

    # Guessing loop
    while attempts_used < max_attempts:
        guess = get_valid_int("Enter your guess: ")
        attempts_used += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts_used} attempts.")
            return

    # If user runs out of attempts
    print(f"Out of attempts! The correct number was {secret_number}.")

# Main program
name = input("Enter your name: ").strip()
print(f"Welcome, {name}! Let's play a guessing game 🎯")

while True:
    play_game()
    again = get_yes_no("Do you want to play again? (y/n): ")
    if again == "n":
        print("Thanks for playing!")
        break
