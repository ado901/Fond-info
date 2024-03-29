'''
 BoardGameGui
 GUI for board games
'''

import g2d
from Hitorigame import *
from time import time

W, H = 40, 40
larghezza, altezza = 10*W, 10*H
LONG_PRESS = 0.5


class BoardGameGui:
    def __init__(self, g: BoardGame):
        self._game = g
        self._downtime = 0
        self.update_buttons()

    def tick(self):
        if g2d.key_pressed("LeftButton"):
            self._downtime = time()
        elif g2d.key_released("LeftButton"):
            mouse = g2d.mouse_position()
            x, y = mouse[0] // W, mouse[1] // H
            if time() - self._downtime > LONG_PRESS:
                self._game.flag_at(x, y)
            else:
                self._game.play_at(x, y)
            self.update_buttons()
        elif g2d.key_pressed("Spacebar"):
            self._game.circle()
            self.update_buttons()
        elif g2d.key_pressed("Enter"):
            self._game.black()
            self.update_buttons()
        elif g2d.key_pressed("w"):
            self._game.solve_recursive(0)
            self.update_buttons()

    def update_buttons(self):
        g2d.clear_canvas()
        g2d.set_color((0, 0, 0))
        cols, rows = self._game.cols(), self._game.rows()
        for y in range(1, rows):
            g2d.draw_line((0, y * H), (cols * W, y * H))
        for x in range(1, cols):
            g2d.draw_line((x * W, 0), (x * W, rows * H))
        for y in range(rows):
            for x in range(cols):
                value = self._game.value_at(x, y)
                center = x * W + W // 2, y * H + H // 2
                x1, y2 = center
                if value[-1] == "#":
                    g2d.fill_rect((x1 - 20, y2 - 20, W, H))
                if value[-1] == "!":
                    g2d.fill_circle(center, H // 2)
                    g2d.set_color((255, 255, 255))
                    g2d.fill_circle(center, H // 2 - 1)
                g2d.set_color((0, 0, 0))
                g2d.draw_text_centered(value[:-1], center, H // 2)
        g2d.update_canvas()
        if self._game.finished():
            g2d.alert(self._game.message())
            g2d.close_canvas()
        errore = self._game.wrong()

        if len(errore) != 0:
            testo = ''
            for i in errore:
                testo += i + ', '
            g2d.alert(testo)


def gui_play(size):

    g2d.init_canvas((int(size) * W, int(size) * H))

    game= HitoriGame(size)
    ui = BoardGameGui(game)
    g2d.main_loop(ui.tick)
