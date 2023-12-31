import time

def print_pause(str):
  print(str)
  time.sleep(2)

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            return response
        elif option2 in response:
            return response
        else:
            print_pause("Sorry, I don't understand.")

def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot. ")
    print_pause("Today we have two breakfasts available. ")
    print_pause("The first is waffles with strawberries and whipped cream. ")
    print_pause("The second is sweet potato pancakes with butter and syrup. ")

def get_order():
    order = valid_input("Please place your order. Would you like waffles or pancakes?\n", "waffles", "pancakes")
    if "waffles" in order:
        print_pause("Waffles it is!")
    elif "pancakes" in order:
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly.")

def order_again():
    order_again = valid_input("Would you like to place another order? Please say 'yes' or 'no'.\n", "yes", "no")
    if "yes" in order_again:
      print_pause("Very good, I'm happy to take another order.")
      get_order()
    elif "no" in order_again:
      print_pause("OK, goodbye!")

def order_breakfast():
    intro()
    get_order()
    order_again()

order_breakfast()


