def count_character(string, target):
  count = 0

  for ch in string:
      if ch == target:
          count += 1

  return count


def start_K(str):
   if str[0] == 'K':
      return True
   else:
      return False
