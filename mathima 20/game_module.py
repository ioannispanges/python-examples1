import random


def roll_dice():
    return random.randint(1, 6)


def play_game(player_name):
    print(f"Welcome , {player_name}! Let's play the game.")
    input("Press Enter to roll the dice....")

    player_roll = roll_dice()
    computer_roll = roll_dice()

    print(f"{player_name} rolled :{player_roll}")
    print(f"Computer rolled: {computer_roll}")

    if player_roll > computer_roll:
        print(f"Congratulations,{player_name}, {player_roll}! You win!")
    elif computer_roll > player_roll:
        print("Computer wins! Better luck next time")
    else:
        print("It's a tie")

    print("Thanks for playing!")
