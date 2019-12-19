import random
import math

n = int(input("dimmi un numero n "))
i = 0
x = 0
y = 0
print("parto dalla posizione x = ", x, " y = ", y)
while i < n:
    passo = random.randint(0, 3)
    if passo == 0:
        y -= 1
    elif passo == 1:
        x += 1
    elif passo == 2:
        y += 1
    else:
        x -= 1
    i += 1
print("Coordinate finali: X = ", x, " Y = ", y)
print("Distanza raggiunta dall'origine: ", abs(x) + abs(y))
