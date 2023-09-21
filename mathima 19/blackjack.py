import random


def deal_card():
    return random.randint(1, 11)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def blackjack():
    print("Welcome to BlackJAck!")

    player_cards = []
    dealer_cards = []

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards:{player_cards}, current score:{player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Do you want to (1) get card or (2) pass ?")
            if should_continue == "1":
                player_cards.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand:{player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

    if player_score > 21:
        print("You went over. You lose!")
    elif dealer_score > 21:
        print("Dealer went over. You win!")
    elif player_score == dealer_score:
        print("It's a draw!")
    elif player_score == 0:
        print("Blackjack! You win!")
    elif dealer_score == 0:
        print("Dealer has blackjack. You lose!")
    elif player_score > dealer_score:
        print("You win!")
    else:
        print("You lose!")


if __name__ == "__main__":
    blackjack()
