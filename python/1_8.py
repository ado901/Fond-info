a = int(input("dimmi un numero "))
denominatore = 0
somma = 0
while a >= 0:
    if a % 2 != 0: #se dispari lo aggiungo alla formula che preparo per la media
        denominatore += 1
        somma += a
    a = int(input("dimmi un numero "))
if denominatore != 0:
    print("la media è: ", somma / denominatore)
else:
    print("divisione per zero")