def text_formatter(text, suround):
    middle = suround * 3 + text + suround * 3
    print(suround * len(middle))
    print(middle)
    print(suround * len(middle))


text_formatter("welcome to the lucky unicorn game","-")
text_formatter("congradulaions you got a unicorn","!")
text_formatter("goodbye","*")
