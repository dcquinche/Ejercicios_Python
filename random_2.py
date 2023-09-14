import random
mood = random.choice(["happy", "sad", "angry", "party"])

import turtle
riley = turtle.Turtle()
riley.width(5)

# Add your code here. El else funciona como componente del último if a no ser que se ponga elif como en este caso para que el else corresponda a todo el bloque de ifs
if mood == "happy":
    riley.color("yellow")
elif mood == "sad":
    riley.color("blue")
elif mood == "angry":
    riley.color("red")
else:
    riley.color("purple")

for side in range(5):
    riley.forward(100)
    riley.right(144)
