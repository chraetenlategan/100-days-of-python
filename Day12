import random
RANDOM_INTEGER = random.randint(1,100)
print("Welcome to my number guessing game \n I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5

found = False
while lives !=0 and found == False:
    print(f"You have {lives} attemps remaining to guess")
    user_input = int(input("Make a guess: "))
    if user_input == RANDOM_INTEGER:
        print(f"Congratiolations, you have won the game, the number was: {RANDOM_INTEGER}")
        found = True
    else:
        lives -=1
        if user_input > RANDOM_INTEGER:
            print("Lower")
        elif user_input < RANDOM_INTEGER:
            print("Higher")

if lives == 0:
    print(f"You have lost the game, the number was : {RANDOM_INTEGER}")
