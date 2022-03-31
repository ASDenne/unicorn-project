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

#main
user_balance = num_function(10, 1, "how much do you want to play with")
print(f"you are playing with ${user_balance}")
