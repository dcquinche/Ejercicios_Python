
try:
  r = requests.get("https://www.udacity.com")
  print(r.text)
except NameError:
  print("Failed for NameError")

string = 'short'
try:
  for letter in range(6):
      print(string[letter])
except IndexError:
   print("Failed for IndexError")

print("Woohoo! You got them all!")
