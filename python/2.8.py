import g2d
from random import randint


class FallingBall:
    def __init__(self, x: int, y: int, A: int):
        self._x = x
        self._y = y
        self._dx = 5
        self._g = 0.4
        self._dy = 0
        self._A = A
        self._r = randint(0, 256)
        self._green = randint(0, 256)
        self._b = randint(0, 256)

    def move(self):
        self._x += self._dx
        self._y += self._dy
        self._dy += self._g
        distance = 20
        if self._x >= self._A - distance:
            self._dx = -5
        if self._x <= 0 + distance:
            self._dx = 5
        if self._y > self._A - distance:
            self._dy = - self._dy
        if self._y < 0 + distance:
            self._dy = -self._dy

    def val(self):
        return self._x, self._y

    def color(self):
        return self._r, self._green, self._b


def update():
    global b, b1
    g2d.clear_canvas()  # Clear background

    g2d.set_color((b.color()))
    g2d.fill_circle((b.val()), 20)  # Draw foreground

    g2d.set_color((b1.color()))
    g2d.fill_circle((b1.val()), 20)

    b.move()
    b1.move()


A = 500
B = 500
g2d.init_canvas((A, B))
b = FallingBall(20, 20, A) # l'esercizio sta tutto qui, nel creare due oggetti invece che uno
b1 = FallingBall(300, 300, A)
g2d.main_loop(update, 30)
