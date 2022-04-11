"""pick random token"""
import random

user=100
tokens = []
for games in range(1,21):
    token = random.randint(1,4)
    if token <= 1:
        user -= 1
        print("donkey")
    elif token <= 2:
        user -= 0.5
        print("horse")
    elif token <= 3:
        user -= 0.5
        print("zebra")
    else:
        user += 4
        print("unicorn")
    print(f"you have played {games + 1} games your balance is {user}")

print(user)

