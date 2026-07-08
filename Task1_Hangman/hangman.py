import random

words = ["python","java","html","css","sql"]

word = random.choice(words)

display = []

for letter in word:
    display.append("_")
 
print("Selected word:", word)
print("hiddern word:", display)

guess = input("Enter a letter: ")
print("you entered:",guess)

if guess in word:
    print("Correct Guess!")
else:
    print("Wrong Guess!")

for position, letter in enumerate(word):
    if letter == guess:
      display[position] = guess

print(display)

