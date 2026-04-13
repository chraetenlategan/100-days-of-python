print("Hello welcome to Chraeten's Blackjack game")
import random 
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
player_cards = []
dealer_cards = []
pick_up = "p"

def show_cards(player_cards,dealer_cards):
    print(f"Your Cards: {player_cards}")
    print(f"The Dealer's cards: {dealer_cards}")

def pick_cards():
    card_deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card_chosen = random.choice(card_deck)
    return card_chosen

def check_21(player_cards,dealer_cards):
    if sum(player_cards)==21 and sum(dealer_cards) == 21:
        print("It was a Draw!!")
        show_cards(player_cards,dealer_cards)
        exit()
    elif sum(player_cards) == 21:
        print("Yobu have won!!")
        show_cards(player_cards,dealer_cards)
        exit()
    elif sum(dealer_cards) == 21:
        print("The dealer has won!!")
        show_cards(player_cards,dealer_cards)
        exit()
    
def check_for_win(player_cards,dealer_cards):
    if sum(player_cards) > sum(dealer_cards) and sum(player_cards) < 21:
        print("You have won!")
        show_cards(player_cards,dealer_cards)
        exit()
    elif sum(player_cards) < sum(dealer_cards):
        print("The Dealer has won!")
        show_cards(player_cards,dealer_cards)
        exit()

def busted(player_cards,dealer_cards):
    if sum(player_cards) > 21:
        print("You are busted")
        show_cards(player_cards,dealer_cards)
        exit()
    elif sum(dealer_cards) > 21:
        print("The dealer is busted")
        show_cards(player_cards,dealer_cards)
        exit()
    else:
        return

def dealer_pickup(dealer_cards):
    while sum(dealer_cards) > 17:
        dealer_cards.append(pick_cards())

play = input("Would you like to play a game of BlackJack y/n").lower()
if play == "n":
    print("See you next time")
    exit()
elif play == "y":
    print(logo)
    for _ in range(2):
        player_cards.append(pick_cards())
        dealer_cards.append(pick_cards())
    check_21(player_cards,dealer_cards)
    dealer_pickup(dealer_cards)
    print(f"Your cards: {player_cards} \n The Dealer's first card : {dealer_cards[0]}")

    while sum(player_cards) < 17:
        print("The player must pick up another card > 17")
        pick_up = input("Press p to pick up a card").lower()
        if pick_up == "p":
            player_cards.append(pick_cards())
            print(f"Your cards are now {player_cards}")
            busted(player_cards,dealer_cards)

    while pick_up == "p":
        pick_up = input("would you like to pick up another card")
        if pick_up == "p":
            player_cards.append(pick_cards())
            print(f"Your cards are now {player_cards}")
            busted(player_cards,dealer_cards)
        else:
            busted(player_cards,dealer_cards)
            check_for_win(player_cards,dealer_cards)

