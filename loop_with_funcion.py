def repeat():
    response = input("Can you guess what my favorite color is?\n")
    if response == 'blue':
        print("That's right! My favorite color is blue.")
    else:
        print("Sorry, that's not my favorite color. Try again!")
        repeat()

repeat()



def green_room():
    print("You are in the green room.")

def blue_room():
    print("You are in the blue room.")

def choose_room():
    choice = input("Would you like to go to the green room or the blue room?\n")
    if choice == 'green':
        green_room()
    elif choice == 'blue':
        blue_room()
    else:
        print("I don't know what that is.")
    choose_room()

choose_room()
