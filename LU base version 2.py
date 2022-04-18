
#instrcutions
import random
#functions
    #yes no checker
def yes_no(question_text):
    while True:
        Answer = input(question_text).lower()
        # if they say output program countiues
        if Answer == "yes" or Answer == "y":
            Answer = "Yes"
            return Answer

        #if they say no output desplay instructions
        elif Answer == "no" or Answer == "n":
            Answer = "No"
            return Answer

        #otherwie show error
        else:
            print('please answer "yes" or "no"')
        print(f"you entered {Answer}")

def instructions():
    print()
    text_formatter("how to play","*")
    print()
    print("choose a starting amount to play with - must be between $1 and $10")
    print()
    print("then press <enter> to play. You will get a random token which might"
          "be a horse, a zebra, a donkey, or a unicorn.")
    print()
    print("It costs $1 to play each round but, depending on your prize, you "
          "could win some of your money back. These are the payout amounts:\n"
          "\tUnicorn: $5 (balance increase by $4\n"
          "\tHorse: $0.50 (balance decrease by $0.50\n"
          "\tZebra: $0.50 (balance decrease by $0.50\n"
          "\tdonkey: $0.00 (balance decrease by $1\n")
    print("\nSee if you can avoid donkeys, get the unicorns, and finish with "
          "more money then you started with.\n")

def num_function(high, low, Question ):
    error = f"must be an integer between {high} and {low}"
    while True:
        try:
            response = int(input(Question))
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

def looping(balance):
    playing = ""


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
            text_formatter("you rolled a donkey",'"')
        #makes horse
        elif token <= 60:
            balance -= 0.5
            roll = "horse"
            text_formatter("you rolled a horse",'>')
        #makes zebra
        elif token <= 90:
            balance -= 0.5
            roll = "zebra"
            text_formatter("you rolled a zebra",'#')
        #makes unicorn
        else:
            balance += 4
            roll = "unicorn"
            text_formatter("congradulaions you got a unicorn","!")
        #print balance
        rounds += 1
        print(f"on round {rounds} you rolled a {roll} your balance now is ${balance}")

    if balance < 1:
        print("sorry you don't have enough money to counitue")
        print()
    print(f"thanks for playing {rounds} games")
    print(f"you started with ${starting}")
    print(f"your balance is ${balance}")
    print(f"you made ${balance - starting}")
    return balance

def text_formatter(text, suround):
    middle = suround * 3 + text + suround * 3
    print(suround * len(middle))
    print(middle)
    print(suround * len(middle))


#mainroutine
text_formatter("welcome to the lucky unicorn game","-")
played_before = yes_no("have you played before? :")
if played_before == "No":
    instructions()
else:
    print("program countiues")
user_balance = num_function(10, 1, "how much do you want to play with")
print(f"you are playing with ${user_balance}")
looping(user_balance)
text_formatter("goodbye","*")
