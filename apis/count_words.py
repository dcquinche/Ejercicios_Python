str = 'it appears that the the appears the most in the sentence'
dict = {}
list = str.split()
count = 1

for item in list:
    if item not in dict:
        dict[item] = 1
    elif item in dict:
        dict[item] += 1

for key, value in dict.items():
    print(f"\'{key}\' appears {value} time(s) in the string")
