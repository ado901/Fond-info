import g2d



class TurningBall:
    def __init__(self, x: int, y: int, A: int, B : int): # A e B sarebbero i valori della canvas, non è necessario passarli, si possono mettere manualmente nel move()
        self._x = x
        self._y = y
        self._dx = 5
        self._dy = 0
        self._A = A
        self._B = B

    def move(self):
        self._x += self._dx
        self._y += self._dy
        distance = 20

        if self._x >= self._A - distance:  # angolo in alto a destra
            self._dx = 0
            self._dy = 5

        if self._y >= self._B - distance:  # angolo in basso a destra
            self._dx = -5
            self._dy = 0
        '''
        nei primi due if posso anche inserire gli and come negli ultimi due ottenendo lo stesso risultato. 
        Non l'ho messo semplicemente per ottimizzare il codice
        '''
        if self._x <= 0 + distance and self._y >= self._B - distance:  # angolo in basso a sinistra
            self._dx = 0
            self._dy = -5

        if self._y <= 0 + distance and self._x <= 0 + distance:  # angolo in alto a sinistra
            self._dx = 5
            self._dy = 0

    def val(self): #mi restituisce le coordinate del centro
        return self._x, self._y


def update():
    global b
    g2d.clear_canvas()  # Clear background
    g2d.fill_circle((b.val()), 20)  #chiamo il metodo di b per avere le coordinate del centro
    b.move()


A = 600
B = 500
g2d.init_canvas((A, B))
b = TurningBall(20, 20, A, B)
g2d.set_color((255, 0, 0))
g2d.main_loop(update, 1000 // 30)
#l'esercizio è identico, c'è solo da ragionare attraverso la classe, niente di più niente di meno