MENU = {
   "espresso": {
       "ingredients": {
           "water": 50,
           "coffee": 18,
       },
       "cost": 1.5,
   },
   "latte": {
       "ingredients": {
           "water": 200,
           "milk": 150,
           "coffee": 24,
       },
       "cost": 2.5,
   },
   "cappuccino": {
       "ingredients": {
           "water": 250,
           "milk": 100,
           "coffee": 24,
       },
       "cost": 3.0,
   }
}


resources = {
   "water": 300,
   "milk": 200,
   "coffee": 100,
}

money = 0

def print_report(resources,money):
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}ml")
    print(f"Money : ${money}")

def check_sufficient(MENU,resources,coffee_chosen):
    ingredients = MENU[coffee_chosen]["ingredients"]

    for item in ingredients:
        if resources[item] < ingredients[item]:
            return False
    return True


coffee_machine = True
while coffee_machine == True:
    print("Welcome to the coffee machine")
    coffee_chosen = input("Would you like an espresso/latte/cappuccino or r for coffee report \n").lower()
    if coffee_chosen == "r":
        print_report(resources,money)
        continue
    if coffee_chosen not in MENU:
        print("Invalid Choice")
        continue
    elif check_sufficient(MENU,resources,coffee_chosen) == False:
        print(f"There is not enough resources for {coffee_chosen}")
        print_report(resources,money)
    else:
        pennies = int(input("How many pennies would you like to give"))
        dimes = int(input("How many dimes would you like to give"))
        dollars = int(input("How many dollars would you like to give"))
        if (dimes/10 + pennies/100 + dollars) == MENU[coffee_chosen]["cost"]:
            money += MENU[coffee_chosen]["cost"]
            print("Here is your coffee:☕")
            resources["water"] -= MENU[coffee_chosen]["ingredients"]["water"]
            resources["milk"] -= MENU[coffee_chosen]["ingredients"]["milk"]
            resources["coffee"] -= MENU[coffee_chosen]["ingredients"]["coffee"]
            order_again = input("Would you like to order agian y/n or type r for report").lower()
            if coffee_chosen == "r":
                print_report(resources,money)
                continue
            if order_again == "n":
                coffee_machine = False
        else:
            print("Not the correct amount of money")
            print("Prices:  espresso(1,5) latte(2,5) cappuccino(3,0)")
            order_again = input("Would you like to order agian y/n").lower()
            if order_again == "n":
                coffee_machine = False

print("Thank you for using the coffee machine")





