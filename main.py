"""
Hangman in python
by Justin Berry
"""

import random

words_short = open("words_short.txt", "r")
words_long = open("words_long.txt", "r")

short_words = []  # List of short words, need to truncate "\n"
long_words = []  # List of long words, need to truncate "\n"

tiles = []  # List of displayed tiles
tiles_word = []  # List of non-displayed tiles, represents letters in the chosen word

letters_tried = []  # Bank of letters already used

punct = "!@#$%^&*()-=+.,/{}[]|<>\\"


def process_words():
    for word in words_short:
        word = word.strip()
        short_words.append(word.lower())

    for word in words_long:
        word = word.strip()
        long_words.append(word.lower())


def assemble_tiles(word):
    for i in range(0, len(word)):
        tiles.append("_")

    for i in tiles:
        print(i, end=" ")


def new_game():
    print ("\n-------------\n")

    tiles_word.clear()
    tiles.clear()
    letters_tried.clear()

    if random.random() < 0.5:
        difficulty = "easy"
        word = random.choice(short_words)
    else:
        difficulty = "hard"
        word = random.choice(long_words)
    assemble_tiles(word)

    for i in word:
        tiles_word.append(i)
    print("\nWelcome to hangman!")
    print("The word you have to guess is", len(word), "letters long.")
    print("Good luck! Your word is", difficulty + ".")


def draw_tiles(bo):
    for i in range(0, len(bo)):
        print(bo[i], end=" ")


def player_pick_letter(letter_bank):
    picking = True
    letter = ""

    while picking:
        letter = str(input("\nGuess a letter: "))
        if len(letter) == 1:
            if letter not in letter_bank:
                if not letter.isnumeric():
                    if letter not in punct:
                        letter_bank.append(letter)
                        for i in range(0, len(tiles_word)):
                            if letter.lower() == tiles_word[i]:
                                tiles[i] = tiles[i].replace(tiles[i], letter)
                            picking = False
                    else:
                        print("Invalid input.")
                else:
                    print("Input cannot be numeric.")
            else:
                print("You already picked that letter!")
        else:
            print("Input has to be one letter only.")

    return letter


def is_wrong(letter):
    if letter not in tiles_word:
        return True
    return False


def print_word():
    word = ''
    for i in tiles_word:
        word += i

    return word


def main():
    new_game()
    game_over = False
    chances = 8

    while not game_over:
        if chances > 0:
            letter = player_pick_letter(letters_tried)
            if is_wrong(letter):
                chances -= 1
                print("Wrong! You have", chances, "chances left!")
            draw_tiles(tiles)
        else:
            printWord = print_word()
            print("\nYou lose!")
            print("The word was", printWord, "\n")
            game_over = True

        if "_" not in tiles:
            print("\nYou win!")
            game_over = True

    play_again = input("Play again? (Y/N) ")
    if play_again.lower() == "y" or play_again.lower() == "yes":
        game_over = False
        main()
    else:
        raise SystemExit()


process_words()
main()
