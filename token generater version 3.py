"""pick random token"""
import random
#money input
balance = 100
#saving input
starting = balance
#starting/ repeating game
for games in range(10):
    #choosing token
    token = random.randint(1,100)
    #makes donkey
    if token <= 30:
        balance -= 1
        print("donkey")
    #makes horse
    elif token <= 60:
        balance -= 0.5
        print("horse")
    #makes zebra
    elif token <= 90:
        balance -= 0.5
        print("zebra")
    #makes unicorn
    else:
        balance += 4
        print("unicorn")
    #print balance
    print(f"you have played {games + 1} games your balance is {balance}")

print(f"${starting}")
print(f"${balance}")
