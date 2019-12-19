import g2d
from Actor import *
import random


bucacont = 0
rocciacont = 0


def update():
    terrenoval = B - 100
    global players
    g2d.clear_canvas()
    global bucacont, boh, rocciacont, rover2
    if arena.stop() is False:
        if g2d.key_pressed("ArrowUp"):
            rover.go_up()
        elif g2d.key_pressed("ArrowDown"):
            rover.go_down()
        elif g2d.key_pressed("Spacebar"):
            x, y, w, h = rover.position()
            Proiettile(arena, x + (w / 4), y, 0, -5)
            Proiettile(arena, x + w, y + (h / 2), 5, 0)
        elif g2d.key_pressed("ArrowRight"):
            rover.go_right()
        elif g2d.key_pressed("ArrowLeft"):
            rover.go_left()
        elif (
                g2d.key_released("ArrowUp") or g2d.key_released("ArrowRight") or g2d.key_released("ArrowLeft")):
            rover.stay()
        if players:
            if g2d.key_pressed("w"):
                rover2.go_up()
            elif g2d.key_pressed("s"):
                rover2.go_down()
            elif g2d.key_pressed("LeftButton"):
                x, y, w, h = rover2.position()
                Proiettile(arena, x + (w / 4), y, 0, -5)
                Proiettile(arena, x + w, y + (h / 2), 5, 0)
            elif g2d.key_pressed("d"):
                rover2.go_right()
            elif g2d.key_pressed("a"):
                rover2.go_left()
            elif (
                    g2d.key_released("w") or g2d.key_released("d") or g2d.key_released("a")):
                rover2.stay()

    arena.move_all()
    g2d.draw_image_clip(image, (0, 0, 512, 128), (0, 0, A, B))
    if random.randint(0, 50) == 0 and \
            bucacont >= 30 and \
            arena.stop() is False and rocciacont >= 30:
        Buca(arena, A)
        bucacont = 0
    if random.randint(0, 50) == 0 and \
            rocciacont >= 30 and \
            arena.stop() is False and bucacont >= 30:
        choice = bool(random.getrandbits(1))
        if choice:
            Roccia(arena, A, terrenoval - 16, choice)
        else:
            Roccia(arena, A, terrenoval - 36, choice)
        rocciacont = 0

    for a in arena.actors():
        if a.symbol() != (0, 0, 0, 0):
            if isinstance(a,
                          Sfondo):  # il discriminante tra gli sfondi e tutto il resto è l'immagine da cui prendere le porzioni symbol
                g2d.draw_image_clip(image, a.symbol(), a.position())
            else:
                g2d.draw_image_clip(sprites, a.symbol(), a.position())
        else:
            g2d.fill_rect(a.position())
    bucacont += 1
    rocciacont += 1


A = 500
B = 600
terrenoval = B - 100
arena = Arena(A, B)

montagne1 = Sfondo(arena, (0, (B - 75) // 3, A, B - (B - 75) // 3), (0, 258, 512, 128), 1)
montagne2 = Sfondo(arena, (A, (B - 75) // 3, A, B - (B - 75) // 3), (0, 258, 512, 128), 1)
città1 = Sfondo(arena, (0, terrenoval - 90, A, B - (terrenoval - 90)), (0, 386, 512, 128), 2)
città2 = Sfondo(arena, (A, terrenoval - 90, A, B - (terrenoval - 90)), (0, 386, 512, 128), 2)
terreno1 = Sfondo(arena, (0, terrenoval, A, 100), (0, 513, 512, 128), 3)
terreno2 = Sfondo(arena, (A, terrenoval, A, 100), (0, 513, 512, 128), 3)

rover = Rover(arena, 100, B - 100)
alien1 = Alien(arena)
alien2 = Alien(arena)

sprites = g2d.load_image("moon-patrol.png")
image = g2d.load_image("moon-patrol-bg.png")

players = False


def main():
    g2d.init_canvas((A, B))
    global players, rover2
    players = g2d.confirm("2 Giocatori?")
    print(players)
    if players:
        rover2 = Rover(arena, 200, B - 100)
    g2d.main_loop(update)



if __name__ == '__main__':
    main()
