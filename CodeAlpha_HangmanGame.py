import random

words = ["python", "code", "intern", "data", "game"]
word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    display = ""
    
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    
    print("\nWord:", display)

    if "_" not in display:
        print("🎉 You won!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    if guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("💀 You lost! The word was:", word)