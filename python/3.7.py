import g2d
from Actor import Actor, Arena, Rover

contatore = 0
contatore2 = 0
contatore3 = 0


def update():
    terrenoval = B - 100
    global contatore, contatore2, contatore3
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

    # -------------------------------------Sfondo-----------------------------------------------------------
    '''Disegno 2 volte l'immagine, di cui una volta fuori dallo schermo, quando il decremento è uguale al totale del canvas lo ripristino in modo
        che il movimento sembri continuo'''
    g2d.draw_image_clip(image, (0, 0, 512, 128), (0, 0, A, B))

    g2d.draw_image_clip(image, (0, 258, 512, 128), (0 - contatore3 // 2, (B - 75) // 3, A, B - (B - 75) // 3))
    g2d.draw_image_clip(image, (0, 258, 512, 128), (A - contatore3 // 2, (B - 75) // 3, A, B - (B - 75) // 3))

    g2d.draw_image_clip(image, (0, 386, 512, 128), (0 - contatore, terrenoval - 90, A, B - (terrenoval - 90)))
    g2d.draw_image_clip(image, (0, 386, 512, 128), (A - contatore, terrenoval - 90, A, B - (terrenoval - 90)))

    g2d.draw_image_clip(image, (0, 513, 512, 128), (0 - contatore2 * 2, terrenoval, A, 100))
    g2d.draw_image_clip(image, (0, 513, 512, 128), (A - contatore2 * 2, terrenoval, A, 100))
    if contatore == A:
        contatore = 0
    if contatore2 == A // 2:
        contatore2 = 0
    if contatore3 == A * 2:
        contatore3 = 0

    for a in arena.actors():
        if a.symbol() != (0, 0, 0, 0):
            g2d.draw_image_clip(sprites, a.symbol(), a.position())
        else:
            g2d.fill_rect(a.position())
    contatore += 1
    contatore2 += 1
    contatore3 += 1


A = 500
B = 600
arena = Arena(A, B)
turtle = Rover(arena, 20, 20, A, B)
sprites = g2d.load_image("moon-patrol.png")
image = g2d.load_image("moon-patrol-bg.png")


def main():
    g2d.init_canvas((A, B))
    g2d.main_loop(update)


if __name__ == '__main__':
    main()
