favorites = {'color': 'purple', 'number': 42, 'animal': 'turtle', 'language': 'python'}

for key in favorites:
    print(key)

for key in favorites.keys():
    print(key)

for item in favorites.values():
    print(item)

for entry in favorites.items():
   print(entry)

for key, value in favorites.items():
    print(key)
    print(value)

for key, value in favorites.items():
	print(f"my favorite {key} is {value}")
