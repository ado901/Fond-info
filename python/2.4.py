import g2d
from random import randint

a = int(input("numero righe?"))
x = 40
y = 40
g2d.init_canvas((600, 600))
for i in range(1, a + 1):

    for k in range(1, i + 1):
        # Blue circle, center=(400, 300), radius=20
        g2d.set_color((randint(0, 256), randint(0, 256), randint(0, 256)))
        g2d.fill_circle((x, y), 20)  # circle
        x += 80
    y += 80
    x = 40
g2d.main_loop()

'''
l'esercizio è lo stesso del 2.3 applicato ai cerchi, ad ogni incremento di riga aumento la y
per ogni cerchio che devo disegnare per riga aumento la x
poi alla fine la riporto al valore iniziale per riallinearsi a sinistra
'''
