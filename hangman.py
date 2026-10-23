import random

words = ["python", "laptop", "coding", "random", "server"]
secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0

# Drawing for 0 to 6 wrong guesses
hangman_stages = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
]

while wrong_guesses < 6:
    print(hangman_stages[wrong_guesses])

    # Show the word, hide letters not guessed yet
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "
    print(display)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess.isalpha() == False:
        print("Please enter a letter, not a number or symbol.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct!")
    else:
        wrong_guesses = wrong_guesses + 1
        print("Wrong! Attempts left:", 6 - wrong_guesses)

    # Check if all letters are guessed
    won = True
    for letter in secret_word:
        if letter not in guessed_letters:
            won = False

    if won == True:
        print("You won! The word was:", secret_word)
        break

# Loop is over, check if the player lost
if wrong_guesses == 6:
    print(hangman_stages[6])
    print("You lost! The word was:", secret_word)