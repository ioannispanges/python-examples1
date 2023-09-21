import game_module


def main():
    print("Dice Game Simulator")
    print("-------------------")

    player_name = input("Enter your name:")
    # round_games = input("Please insert rounds:")
    game_module.play_game(player_name)


if __name__ == "__main__":
    main()
