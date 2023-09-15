def start_K(str):
   if str[0] == 'K':
      return True
   else:
      return False


def start_with(str1, str2):
   if str1[0] == str2[0]:
      return True
   else:
      return False

def start_with_v2(long, short):
    for i in range(len(short)):
      if long[i] != short[i]:
         return False
    return True

def start_with_v3(long, short):
    if long[0:len(short)] == short:
        return True
    else:
       return False

def good_length(password):
   return len(password) >= 8 and len(password) <= 64

def total_length(list):
    total = 0
    for item in list:
        total = total + len(item)
    return total
