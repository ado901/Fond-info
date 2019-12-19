import g2d
from random import randint

n = int(input("inserire numero rettangoli: "))
g2d.init_canvas((600, 400))
i = 0
while i < n:
    a = randint(1, 500)
    b = randint(1, 300)
    c = randint(1, 200)
    d = randint(1, 200)
    g2d.set_color((150, 150, 150))  # prima disegno le ombre leggermente spostate (luce direzionale) e poi disegno i rettangoli
    g2d.fill_rect((a + 5, b + 5, c, d))
    g2d.set_color((randint(1, 255), randint(1, 255), randint(1, 255)))  # color
    g2d.fill_rect((a, b, c, d))  # rect

    i += 1

g2d.main_loop()
