"""pick random token"""
import random
balance = 100
starting = balance
for games in range(100):
    token = random.randint(1,100)
    if token <= 30:
        balance -= 1
        print("donkey")
    elif token <= 60:
        balance -= 0.5
        print("horse")
    elif token <= 90:
        balance -= 0.5
        print("zebra")
    else:
        balance += 4
        print("unicorn")
    print(f"you have played {games + 1} games your balance is {balance}")
print(f"${starting}")
print(f"${balance}")
