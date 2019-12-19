import g2d


class TurningBall:
    def __init__(self, x: int, y: int, A: int, B: int):  # A e B sarebbero i valori della canvas, non è necessario passarli, si possono mettere manualmente nel move()
        self._x = x
        self._y = y
        self._dx = 5
        self._dy = 0
        self._A = A
        self._B = B

    def move(self, i: int):
        self._x += self._dx
        self._y += self._dy

        if i == 10:  # angolo in alto a destra
            self._dx = 0
            self._dy = 10

        if i == 20:  # angolo in basso a destra
            self._dx = -10
            self._dy = 0

        if i == 30:  # angolo in basso a sinistra
            self._dx = 0
            self._dy = -10

        if i == 40:  # angolo in alto a sinistra
            self._dx = 10
            self._dy = 0

    def val(self):  # mi restituisce le coordinate del centro
        return self._x, self._y


def update():
    global b, i
    i += 1
    g2d.clear_canvas()  # Clear background
    g2d.fill_circle((b.val()), 20)  # chiamo il metodo di b per avere le coordinate del centro
    b.move(i)
    if i == 40:
        i = 0


A = 600
B = 500
i = 0
g2d.init_canvas((A, B))
b = TurningBall(300, 200, A, B)
g2d.set_color((255, 0, 0))
g2d.main_loop(update, 30)
