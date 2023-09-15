def until_dot(str):
  index = 0
  while str[index] != '.':
    index += 1
  return str[:index]

print(until_dot("Udacity.com"))
