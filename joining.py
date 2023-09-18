#lines = ["Haiku frogs in snow",
#         "A limerick came from Nantucket",
#         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

#def breakify(strings):
#    return "<br>".join(strings)

#print(breakify(lines))


string = "Hello world!"
output = [] # Create empty list
index = 0
while index < len(string):
    output.append(string[index]) # Append current character
    index += 1 # Move on to next character

print(output)


def remove_substring(string, substring):
    output = []
    index = 0
    while index < len(string):
      if string[index:index+len(substring)] == substring:
          index += len(substring)
      else:
          output.append(string[index])
          index += 1
    return "".join(output)

print(remove_substring('SPAM!HelloSPAM! worldSPAM!!', 'SPAM!'))



def replace_substring(string, substring, replacement):
    output = []
    index = 0
    while index < len(string):
      if string[index:index+len(substring)] == substring:
          output.append(replacement)
          index += len(substring)
      else:
          output.append(string[index])
          index += 1
    return "".join(output)

print(replace_substring('Hot SPAM!drop soup, and curry with SPAM!plant.', 'SPAM!', 'egg'))
