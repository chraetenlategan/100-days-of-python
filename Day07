import random
# Chraeten Hang Man game
print("Welcome to Chraeten's game of Hangman")

words = ["cat", "cat"]
random_word = random.choice(words)
censored = len(random_word)*"_"
print(f"Your random word is \n {censored}")

lives = 3
while random_word != censored and lives != 0:
    bfound = False
    user_input = input(f"Pick a letter \n")
    for i in range(len(random_word)):
        if user_input == random_word[i]:
            bfound = True
            censored = censored[:i] + user_input + censored[i+1:]
            print(f" correct !!! \n {censored}")
    if bfound == False:
        lives -= 1
        print(f"Incorrect Letter you have {lives} lives left")

if censored == random_word:
    print(f"Congrationlations you have won the game with {lives} lives left")
else:
    print(f"Unlucky you ran out of lives, the word was {random_word}")
