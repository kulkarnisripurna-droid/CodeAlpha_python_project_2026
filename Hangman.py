import random

# Predefined words list
words = ["apple", "tiger", "chair", "robot", "pizza"]

# Choose random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum wrong guesses
wrong_guesses = 0
max_wrong = 6

# Display hidden word
display = ["_"] * len(word)

print("=== HANGMAN GAME ===")

# Game loop
while wrong_guesses < max_wrong and "_" in display:
    
    print("\nWord:", " ".join(display))
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check letter in word
    if guess in word:
        print("Correct!")

        # Reveal letters
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        print("Wrong guess!")
        wrong_guesses += 1

# Final result
if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)