import g2d
from Actor import Actor, Arena


class Rover(Actor):
    ''' Tartaruga: movimento guidato dai tasti freccia
        non supera i bordi dell'arena
    '''

    def __init__(self, arena , x, y, arena_w, arena_h):
        self._x, self._y = x, y
        self._w, self._h = 20, 20
        self._speed = 10
        self._dx, self._dy = 0, 0
        self._arena = arena
        self._arena.add(self)
        self._arena_w = arena_w
        self._arena_h = arena_h
        self._g = 0.4

    def move(self):
        self._y += self._dy
        self._dy += self._g
        if self._y < 0:
            self._y = 0
            self._dy = self._speed
        elif self._y > self._arena_h - self._h:
            self._y = self._arena_h - self._h
            self._dy = 0

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > self._arena_w - self._w:
            self._x = self._arena_w - self._w

    def go_left(self):
        self._dx, self._dy = -self._speed, 0

    def go_right(self):
        self._dx, self._dy = +self._speed, 0

    def go_up(self):
        if self._dy == 0:
            self._dx, self._dy = 0, -self._speed
        else:
            pass

    def go_down(self):
        self._dx, self._dy = 0, +self._speed

    def stay(self):
        self._dx, self._dy = 0, 0

    def collide(self, other):
        pass

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        ''' sprite coordinate 0,0 20,20 '''
        return 0, 0, 0, 0


def update():
    if g2d.key_pressed("ArrowUp"):
        turtle.go_up()
    elif g2d.key_pressed("ArrowRight"):
        turtle.go_right()
    elif g2d.key_pressed("ArrowDown"):
        turtle.go_down()
    elif g2d.key_pressed("ArrowLeft"):
        turtle.go_left()
    elif (
          g2d.key_released("ArrowRight") or
          g2d.key_released("ArrowDown") or
          g2d.key_released("ArrowLeft")):
        turtle.stay()

    arena.move_all()
    g2d.clear_canvas()
    for a in arena.actors():
        if a.symbol() != (0, 0, 0, 0):
            print(a.symbol())
            g2d.draw_image_clip(sprites, a.symbol(), a.position())
        else:
            g2d.fill_rect(a.position())


A = 500
B = 500
arena = Arena(A, B)
turtle = Rover(arena, A - 20, B - 20, A, B)
sprites = g2d.load_image("moon-patrol.png")


def main():
    g2d.init_canvas((A, B))
    g2d.main_loop(update)


main()
