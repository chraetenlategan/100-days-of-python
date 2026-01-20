import random
rock = '''
   _______
---'   ____)
     (_____)
     (_____)
     (____)
---.__(___)
'''


paper = '''
   _______
---'   ____)____
         ______)
         _______)
        _______)
---.__________)
'''


scissors = '''
   _______
---'   ____)____
         ______)
      __________)
     (____)
---.__(___)
'''
options = [rock,paper,scissors]

print("Welcome to a game of rock paper scissors")
user_input = input("Please select R,P,S")

#Display users choice
print("Your selection")
if user_input == "R":
   print(rock)
elif user_input == "S":
   print(scissors)
elif user_input == "P":
   print(paper)
else:
   print("Please enter a valid letter")

#Display the bot's choice
print("Bot selection")
bot_chosen = random.randint(1,3)
if bot_chosen == 1:
   print(rock)
elif bot_chosen ==2:
   print(paper)
else:
   print(scissors)

#Compare to see who win

#Draw
if ((bot_chosen == 1)and(user_input == "R")) or ((bot_chosen == 2)and(user_input == "P")) or ((bot_chosen == 3)and(user_input == "S")):
   print("It is a draw")
elif (bot_chosen == 1 and user_input == "S") or (bot_chosen == 2 and user_input == "R") or (bot_chosen == 3 and user_input =="P"):
   print("The randomize bot has won ")
else:
   print("Congratulations, you have won!")


