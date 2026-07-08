import random

# List of words
words = ["python", "java", "html", "css", "sql"]

# Choose a random word
word = random.choice(words)

# Uncomment this line only for testing
print("Selected Word:", word)

# Create hidden display
display = []

for letter in word:
    display.append("_")

print("Hidden Word:", " ".join(display))

game_over = False

while not game_over:

    guess = input("\nEnter a letter: ").lower()

    if guess in word:
        print("✅ Correct Guess!")

        # Reveal the guessed letter
        for position in range(len(word)):
            if word[position] == guess:
                display[position] = guess
    else:
        print("❌ Wrong Guess!")

    print("Word:", " ".join(display))

    # Check if player has guessed all letters
    if "_" not in display:
        print("\n🎉 Congratulations! You Won!")
        game_over = True