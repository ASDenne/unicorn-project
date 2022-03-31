#instrcutions

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
    print("***how to play***")
    print()
    print("instructions")
    print()
    print("countiue to game")

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


#mainroutine
played_before = yes_no("have you played before? :")
if played_before == "No":
    instructions()
else:
    print("program countiues")
user_balance = num_function(10, 1, "how much do you want to play with")
print(f"you are playing with ${user_balance}")
