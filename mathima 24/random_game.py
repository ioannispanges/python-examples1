import random


def play_game():
    choices = ["rock", "paper", "scissors"]

    player1 = input("Player 1, enter your choice (rock/paper/scissors): ").lower()
    player2 = random.choice(choices)

    print(f"Player2 chose :{player2}")

    if player1 not in choices:
        print("Invalid input")
        return

    if player1 == player2:
        print("It's a tie!")
    elif (
            (player1 == "rock" and player2 == "scissors") or
            (player1 == "paper" and player2 == "rock") or
            (player1 == "scissors" and player2 == "paper")
    ):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors")
    while True:
        play_game()
        play_again = input(" Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
