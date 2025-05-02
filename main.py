#import libraries
import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

print(logo)
lives = 6
chosen_word = random.choice(word_list)

print(chosen_word)

placeholder = " "
for letter in chosen_word:
    placeholder += "_"
print(placeholder)


display = ["_"]*len(chosen_word)
guessed_letters = []
while lives > 0 and "_" in display:
    correct_guess = False
    guess = input("guess a letter:").lower()
    if guess in guessed_letters:
        print(f"You've already guessed: {guess}")
    else:
        guessed_letters.append(guess)

        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess
                correct_guess = True
        joined_list = "".join(display)
        print(joined_list)
        if correct_guess == False:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            print(f"****************************{lives} LIVES LEFT****************************")
        if lives == 6:
            print(stages[6])
        elif lives == 5:
            print(stages[5])
        elif lives == 4:
            print(stages[4])
        elif lives == 3:
            print(stages[3])
        elif lives == 2:
            print(stages[2])
        elif lives == 1:
            print(stages[1])
        else:
            print(stages[0])

if joined_list == chosen_word:
    print("You win!")
else:
    print(f"It was {chosen_word}! You loose :(")
