word = "definitely"
length = len(word)

for n in range(length):
    print(word[:n+1])

for n in range(length):
    print(word[:length-n])
