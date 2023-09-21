import random


def choose_word():
    word_list = ["python", "programming", "computer", "keyboard", "elephant", "banana"]

    return random.choice(word_list)


def display_word(word, guessed_letters):
    display = " "
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = [0, -1]

    guessed_letters.append(secret_word[0])

    guessed_letters.append(secret_word[-1])
    # print(guessed_letters)


    attemps = 6

    while attemps > 0:
        print("\n" + display_word(secret_word, guessed_letters))
        guess = input("Guess a letter:   ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter. ")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct")
            if secret_word == display_word(secret_word, guessed_letters):
                print(f"Congratulations! You have guessed the word '{secret_word}'!")
                break
        else:
            attemps -= 1
            print(f"Incorrect! You have {attemps} attempts remaing. ")

        if attemps == 0:
            print(f"Sorry, you have run out of attemps. The word was '{secret_word}'.")


if __name__ == "__main__":
    hangman()
