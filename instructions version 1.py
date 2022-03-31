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

#mainroutine
played_before = yes_no("have you played before? :")
if played_before == "No":
    instructions()
else:
    print("program countiues")

