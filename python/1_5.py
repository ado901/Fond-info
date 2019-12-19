import g2d

A = 800
g2d.init_canvas((A, A))
n = int(g2d.prompt("Numero di quadrati? "))
i = 0
c_increment = 255 // n
l_increment = A // n  # suddivido la canvas e il colore blu in n parti che faranno da incremento

while i < n:
    g2d.set_color((0, 0, c_increment * i))  # color
    g2d.fill_rect((0, 0, l_increment * (n - i), l_increment * (n - i)))
    i += 1
g2d.main_loop()
