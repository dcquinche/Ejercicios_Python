def is_substring(substring, string):
    index = 0
    while index < len(string):
        if string[index : index + len(substring)] == substring:
            return True
        index += 1
    return False

print(is_substring('ff', 'waffle'))

def count_substring(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
        index += 1
    return total

print(count_substring('love, love, love, all you need is love', 'love'))

def count_substring_v2(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
            index += len(target)
        else:
            index += 1
    return total


def locate_all(string, target):
    index = 0
    list = []
    while index < len(string):
        if string[index : index + len(target)] == target:
            list.append(index)
            index += len(target)
        else:
            index += 1
    return list

print(locate_all('cookbook', 'ook'))
