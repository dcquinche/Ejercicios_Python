import time

n = 10
while n >= 1:
  print(n)
  n -= 1
  time.sleep(1)
print("Blastoff!")

s = "Tenochtitlan"
index = 0
while index < len(s):
    print(s[:index])
    index += 1

s = "abracadabra"
index = 0
while index < len(s):
    print(s[:len(s)-index])
    index += 1
