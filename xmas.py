import webbrowser


one = "          *"
three ="         ***"
five = "        *****"
seven = "       *******"
eleven = "     ***********"
fifteen = "   ***************"
twentyone = "*********************"


def make_tree():
    print(one)
    print(three)
    print(five)
    print(seven)
    print(three)
    print(seven)
    print(eleven)
    print(fifteen)
    print(five)
    print(eleven)
    print(fifteen)
    print(twentyone)
    print(three)
    print(three)    


make_tree()

print("For more x-mas press (M), press (Q) for quit.")
while (True):
    answer = input()
    if answer.upper()  == "M":
        break
    elif answer.upper() == "Q":
        exit()
    else:
        print("Press (M) for more x-mas or (Q) for quit, fool!!!")


one = "    .     Ä   . --x"
three =" .   . . ***    .   ."
five = ".    .  *o***  ."
seven = "   .   ****o**  ."
eleven = "     *o****o***    ."
fifteen = " . ***********o*** ."
twentyone = "***o***************o*"


make_tree()


print("OK, wanna x-mas it up??? Press (Y) if you are cool or press (Q) if you suck.")
while (True):
    answer = input()
    if answer.upper() == "Y":
        break
    elif answer.upper() == "Q":
        exit()
    else:
        print("Press (Y) for more x-mas or (Q) for quit, you know the game!!!")


make_tree()

webbrowser.open("https://www.youtube.com/watch?v=E8gmARGvPlI?autoplay=1")

