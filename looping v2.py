import random
playing = ""

balance = 5
starting = balance
rounds = 0
roll = ""
while balance >= 1:
    print("press <enter> to play or <x> to exit")
    playing = input(">>")
    while playing != "" and playing != "x":
        print('please press enter or "X"')
        print("press <enter> to play or <x> to exit")
        playing = input(">>")
    if playing == "x":
        break
    token = random.randint(1,100)
     #makes donkey
    if token <= 30:
        balance -= 1
        roll = "donkey"
    #makes horse
    elif token <= 60:
        balance -= 0.5
        roll = "horse"
    #makes zebra
    elif token <= 90:
        balance -= 0.5
        roll = "zebra"
    #makes unicorn
    else:
        balance += 4
        roll = "unicorn"
    #print balance
    rounds += 1
    print(f"on round {rounds} you rolled a {roll} your balance now is ${balance}")

if balance < 1:
    print("sorry you don't have enough money to counitue")
    print()
print(f"thanks for playing {rounds} games")
print(f"your balance is {balance}")
print(f"you made ${balance - starting}")
print("goodbye")
