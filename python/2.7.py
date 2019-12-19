import g2d


class FallingBall:
    def __init__(self, x: float, y: float, A: int):
        self._x = x
        self._y = y
        self._dx = 5
        self._g = 0.4
        self._dy = 0
        self._A = A

    def move(self):
        self._x += self._dx
        self._y += self._dy
        self._dy += self._g
        distance = 20
        if self._x >= self._A - distance:  #non necessario al fine dell'esercizio
            self._dx = -5
        if self._x <= 0 + distance: #non necessario al fine dell'esercizio
            self._dx = 5
        if self._y > self._A - distance:
            self._dy = - self._dy
        if self._y < 0 + distance: #non necessario al fine dell'esercizio
            self._dy = -self._dy
        '''
        concettualmente l'esercizio è abbastanza guidato, ti viene già detto come gestire fare per simulare la gravità
        g rimane invariato, quando la y tocca il pavimento la dy (quindi la velocità) viene invertita'''

    def val(self):
        return self._x, self._y


def update():
    global b
    g2d.clear_canvas()  # Clear background
    g2d.fill_circle((b.val()), 20)  # Draw foreground
    b.move()


A = 500
B = 500
g2d.init_canvas((A, B))
b = FallingBall(20, 20, A)
g2d.set_color((255, 0, 0))
g2d.main_loop(update, 1000 // 30)
