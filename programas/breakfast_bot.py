import time

print("Hello! I am Bob, the Breakfast Bot. ")
time.sleep(2)
print("Today we have two breakfasts available. ")
time.sleep(2)
print("The first is waffles with strawberries and whipped cream. ")
time.sleep(2)
print("The second is sweet potato pancakes with butter and syrup. ")
time.sleep(2)

while True:
  while True:
    order = input("Please place your order. Would you like waffles or pancakes?\n").lower()
    if "waffles" in order:
      time.sleep(2)
      print("Waffles it is!")
      break
    elif "pancakes" in order:
      time.sleep(2)
      print("Pancakes it is!")
      break
    else:
      time.sleep(2)
      print("Sorry, I don\'t understand.")

  time.sleep(2)
  print("Your order will be ready shortly.")
  time.sleep(2)
  while True:
    order_again = input("Would you like to place another order? Please say 'yes' or 'no'.\n").lower()
    if "yes" in order_again:
      time.sleep(2)
      print("Very good, I'm happy to take another order.")
      break
    elif "no" in order_again:
      time.sleep(2)
      print("OK, goodbye!")
      break
    else:
      time.sleep(2)
      print("Sorry, I don\'t understand.")
  if "no" in order_again:
    break
