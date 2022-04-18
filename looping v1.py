playing = ""
balance = 10
starting = balance
rounds = 0
while balance >= 1:
    print("press <enter> to play")
    playing = input(">>")
    while playing != "" and playing != "x":
        print('please press enter or "X"')
        print("press <enter> to play")
        playing = input(">>")
    if playing == "x":
        break
    rounds += 1
    balance -= 1
    print(f"on round {rounds} you rolled a donkey your balance now is ${balance}")

print(f"thanks for playing {rounds} games")
print(f"your balance is {balance}")
print(f"you made ${balance - starting}")
