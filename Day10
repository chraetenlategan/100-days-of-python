print("Welcome to my calculator app")
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def divide(n1,n2):
    return(n1/n2)
def multiply(n1,n2):
    return(n1*n2)

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

inum1 = float(input("What is your first number  "))
while True:
    operation_chosen = input("+ \n - \n / \n * Pick an operation    ")
    inum2 = float(input("What is your next number   "))
    result = operations[operation_chosen](inum1,inum2)
    print(f"{inum1} {operation_chosen} {inum2} = {result}")
    change =input(f"Type y to continue with {result} or n to start new calculation")
    if change == "y":
        inum1 = result
    elif change == "n":
        inum1 = float(input("What is your first number  "))

