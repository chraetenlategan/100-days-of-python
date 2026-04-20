balance = 60.9
while True:
    try:
        num = float(input("What is deposit: "))
        break
    except ValueError:
        print("must be a valid quantity")

balance += num

print(f"Your new balance is : {balance}")