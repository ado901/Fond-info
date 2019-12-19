import g2d

A = 500
B = 500
n = float(input("inserire valore: "))
lista = []
maggiore = 0
contatore = 0
while n >= 0:
    lista.append(n)
    contatore += 1
    if n > maggiore:
        maggiore = n
    n = float(input("inserire valore: "))

g2d.init_canvas((A, B))
x = 0
y = 0
d_y = B // contatore
g2d.set_color((0, 0, 255))
for k, val in enumerate(lista):
    g2d.fill_rect((0, y, (val * A) / maggiore, d_y - 5))
    y += d_y
g2d.main_loop()
