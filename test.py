# ask the user if they have played before
show_instructions = input("have you played before? :").lower()
# if they say output program countiues
if show_instructions == "yes":
    print("program countinues")

#if they say no output desplay instructions
elif show_instructions == "no":
    print("display instructions")

#otherwie show error
else:
    print('please answer "yes" or "no"')
