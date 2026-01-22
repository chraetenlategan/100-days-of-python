print("Welcome to my silent auction game")
auctions = {}
highest_bids ={}
highest = 0
bidders = ""
another_person = "yes"
while another_person == "yes":
    name = input("What is your name \n")
    amount = int(input("What amount do you want to bid \n"))
    another_person = input("Is there another person who want to bid \n").lower()
    auctions[name] = amount

for name in auctions:
    if auctions[name]>highest:
        highest = auctions[name]
        highest_bids.clear()
        highest_bids[name] = highest
    elif auctions[name] == highest:
        highest_bids[name] = highest

if len(highest_bids) == 1:
    print(f"The Highest bidder was {highest_bids} with a bid of {highest}")
else:
    for names in highest_bids:
        bidders += names + ' '
    print(f"The higherst bidders were {bidders} with a bid of {highest}")
    
