playing = ""
balance = 10
while playing != "x" and balance:
    print("press <enter> to play")
    playing = input(">>")
    while playing != "" and playing != "x":
        print('please press enter or "X"')
        print("press <enter> to play")
        playing = input(">>")

