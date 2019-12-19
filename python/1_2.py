import math

a = float(input("inserire raggio sfera: "))
b = float(input("inserire densità sfera: "))
print("Superficie: ", 4 * math.pi * a ** 3, "\n Volume: ", 4 / 3 * math.pi * a ** 3, "\n Peso: ",
      b * (4 / 3 * math.pi * a ** 3))
