import random
import hangman_words
import hangman_arts
print(hangman_arts.logo)
print("Lets start the game ")
lives = 6

# Creating the list of name
stages=hangman_arts.stages
world_list = hangman_words.word_list

# randomly choosing the word from list
chosen_word = random.choice(world_list)
print(chosen_word)

word_length = len(chosen_word)

# creating empty list
display=["_" for _ in range(word_length)]
# display=[]
# for i in chosen_word:
#     display+="_"

# Asking user to  guess the letter
while True:
    guess = input("Guess a letter :   ").lower()

    if guess in display:
        print(f"you have already guess this letter {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            print(f"You have guess {guess},is present in word")
            display[position] = letter
            print(stages[lives])
            print(display)


    if guess not in chosen_word:
        lives -= 1
        print(f"You have guess {guess} ,is not present in word you loss a life")
        print(f"{stages[lives]}")
        if lives == 0:
            print("Oops you have loss the game!no lives left ")
            break

    if "_" not in display:
        print("you have win the game")
        print(display)
        break

