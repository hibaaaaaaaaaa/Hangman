import tkinter as tk
import random
from hangman_words import word_list
from hangman_art import logo, stages

#Game setup
lives = 6
chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)
guessed_letters = []

#GUI setup
root = tk.Tk()
root.title("Hangman Game")

#logo on the console
print(logo)

#display the word
display_label = tk.Label(root, text=" ".join(display), font=("Helvetica", 24))
display_label.pack(pady=10)

#message lable for feedback
message_label = tk.Label(root, text="", font=("Helvetica", 14))
message_label.pack()

#lives label
lives_label = tk.Label(root, text=f"Lives: {lives}", font=("Helvetica", 14))
lives_label.pack(pady=10)

#ASCII art label
art_label = tk.Label(root, text=stages[lives], font=("Courier", 10), justify="left")
art_label.pack()

#entry for user guess
entry = tk.Entry(root, font=("Helvetica", 16))
entry.pack()

#hand guess function
def handle_guess():
    global lives
    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if not guess or len(guess) != 1 or not guess.isalpha():
        message_label.config(text="Enter a single valid letter.")
        return

    if guess in display or guess in guessed_letters:
        message_label.config(text=f"You already guessed '{guess}'. No life lost.")
        return

    guessed_letters.append(guess)
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        display_label.config(text=" ".join(display))
        message_label.config(text=f"Correct! '{guess}' is in the word.")
    else:
        lives -= 1
        lives_label.config(text=f"Lives: {lives}")
        art_label.config(text=stages[lives]) 
        message_label.config(text=f"Wrong! '{guess}' is not in the word.")

    #win or loose condition
    if "_" not in display:
        message_label.config(text="🎉 You won!")
        entry.config(state='disabled')
        guess_button.config(state='disabled')
    elif lives == 0:
        message_label.config(text=f"💀 You lost! The word was: {chosen_word}")
        entry.config(state='disabled')
        guess_button.config(state='disabled')

#guess button
guess_button = tk.Button(root, text="Guess", command=handle_guess)
guess_button.pack(pady=10)

#run gui loop
root.mainloop()
