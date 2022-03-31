error = "must be an integer between 1 and 10\n"
valid = False
user_balance = 0
while not 1 <= user_balance <= 10:
    try:
        user_balance= int(input("how much do you want to play with (must be an integer between 1 and 10) $"))
        print()
    except ValueError:
        print(error)
print(f"you are playing with ${user_balance}")
