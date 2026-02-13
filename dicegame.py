"""
this is a gam eof dice rolling.
you will roll and the computer will roll
the winner gets points.
"""
import random

def roll_dice() -> int:
    """
    Will return a random number between 1 and 20.
    """
    randnum = random.randint(1, 20)
    return randnum


def play():
    player_roll=roll_dice()
    computer_roll=roll_dice()


    if player_roll > computer_roll:
        return 1

    elif player_roll < computer_roll:
        return -1

    else:
        return 0
    
player_score = 0
computer_score = 0

 # make a loop first
while player_score < 3 and computer_score < 3:
    result = play()
    if result == 1:
        print("You win this round!")
        player_score += 1
    elif result == -1:
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("It's a tie! No points awarded.")
    

#print final score and say goodbye beta
print(f"Final score: You {player_score} - Computer {computer_score}")
print("Thanks for playing! Goodbye!")