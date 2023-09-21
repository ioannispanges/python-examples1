def display_word(word, guessed_letters):
    display = word[0]
    for letter in word[1:]:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def display_word(word, guessed_letters):
    display = ""
    for index, letter in enumerate(word):
        if letter in guessed_letters or index == 0 or index == 2:  # deikse to 1 kai to 3 gramma
            display += letter
        else:
            display += "_"
    return display