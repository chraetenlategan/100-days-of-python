import random
import art
import data
print(art.logo)

#get first two people
score = 0
correct = True
data_a = random.randint(0,49)
data_b = random.randint(0,49)

print(f"Compare A: {data.stats[data_a]["name"]}, a {data.stats[data_a]["description"]}, from {data.stats[data_a]["country"]}")
print(art.vs)
print(f"Compare B: {data.stats[data_b]["name"]}, a {data.stats[data_b]["description"]}, from {data.stats[data_b]["country"]}")


while correct == True:
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_input == "a" and data.stats[data_a]["follower_count"]< data.stats[data_b]["follower_count"]:
        print(f"Sorry that is wrong. Final Score: {score}")
        correct = False
    elif user_input == "b" and data.stats[data_a]["follower_count"]> data.stats[data_b]["follower_count"]:
        print(f"Sorry that is wrong. Final Score: {score}")
        correct = False
    elif user_input == "a" and data.stats[data_a]["follower_count"]> data.stats[data_b]["follower_count"]:
        score += 1
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"That is correct your score is : {score}")
        data_a = data_b
        data_b = random.randint(0,49)
        print(f"Compare A: {data.stats[data_a]["name"]}, a {data.stats[data_a]["description"]}, from {data.stats[data_a]["country"]}")
        print(art.vs)
        print(f"Compare B: {data.stats[data_b]["name"]}, a {data.stats[data_b]["description"]}, from {data.stats[data_b]["country"]}")
    elif user_input == "b" and data.stats[data_a]["follower_count"]< data.stats[data_b]["follower_count"]:
        score += 1
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"That is correct your score is : {score}")
        data_a = data_b
        data_b = random.randint(0,49)
        print(f"Compare A: {data.stats[data_a]["name"]}, a {data.stats[data_a]["description"]}, from {data.stats[data_a]["country"]}")
        print(art.vs)
        print(f"Compare B: {data.stats[data_b]["name"]}, a {data.stats[data_b]["description"]}, from {data.stats[data_b]["country"]}")

