import g2d
from random import randint

a = int(input("numero righe?"))
x = 300
y = 40
g2d.init_canvas((600, 600))
for i in range(1, a + 1): #in che riga siamo?
    if i % 2 != 0:  # riga dispari
        g2d.set_color((randint(0, 256), randint(0, 256), randint(0, 256))) # disegno il cerchio centrale
        g2d.fill_circle((x, y), 20)  # circle
        for u in range(1, (i // 2) + 1): #ad ogni iterazione disegno un cerchio traslato di 80 a destra e uno di 80 a sinistra (per questo dimezzo i)
            g2d.set_color((randint(0, 256), randint(0, 256), randint(0, 256)))
            g2d.fill_circle((x + 80 * u, y), 20)  # circle
            g2d.set_color((randint(0, 256), randint(0, 256), randint(0, 256)))
            g2d.fill_circle((x - 80 * u, y), 20)  # circle
    else: #riga pari
        x1 = x + 40
        x2 = x - 40
        for u in range(0, i // 2): #disegno un cerchio a destra e uno a sinistra traslati di 80
            g2d.set_color((randint(0, 256), randint(0, 256), randint(0, 256)))
            g2d.fill_circle((x2 - 80 * u, y), 20)  # circle
            g2d.set_color((randint(0, 256), randint(0, 256), randint(0, 256)))
            g2d.fill_circle((x1 + 80 * u, y), 20)  # circle
    y += 80
    x = 300
g2d.set_color((randint(0, 256), randint(0, 256), randint(0, 256)))
g2d.fill_circle((x, y), 20)
g2d.main_loop()

'''
l'esercizio è difficile e particolare, non è immediato, ci si arriva sbagliando e aggiustando il tiro
in sintesi si può descrivere l'albero in questo modo:
per ogni riga dispari abbiamo un cerchio centrale e n-1 cerchi traslati a destra e a sinistra
per ogni riga pari abbiamo n cerchi traslati rispettivamente a sinistra e a destra
e infine abbiamo un cerchio come ultima riga in mezzo
alcune potrebbero essere strane, ho risolto l'esercizio aggiustando il tiro basandomi su cosa mi restituiva il programma'''
