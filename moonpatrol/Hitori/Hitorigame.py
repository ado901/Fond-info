import random


def abstract():
    raise NotImplementedError("Abstract method")


class BoardGame:
    def play_at(self, x: int, y: int): abstract()

    def flag_at(self, x: int, y: int): abstract()

    def value_at(self, x: int, y: int) -> str: abstract()

    def cols(self) -> int: abstract()

    def rows(self) -> int: abstract()

    def finished(self) -> bool: abstract()

    def message(self) -> str: abstract()


def print_game(game: BoardGame):
    for y in range(game.rows()):
        for x in range(game.cols()):
            print('{:3}'.format(game.value_at(x, y)), end='')
        print()


def console_play(game: BoardGame):
    print_game(game)

    while not game.finished():
        x, y = input().split()
        game.play_at(int(x), int(y))
        print_game(game)

    print(game.message())


class HitoriGame(BoardGame):
    def __init__(self, side=5, level=4):
        self._cols, self._rows = side, side
        self._board = [[random.randint(1, 9) for y in range(side)] for x in range(side)]
        self._board2 = [["CLEAR" for y in range(side)] for x in range(side)]

    def cols(self) -> int:
        return self._cols

    def rows(self) -> int:
        return self._rows

    def play_at(self, x: int, y: int):
        if 0 <= x < self._cols and 0 <= y < self._rows:
            if self._board2[x][y] == "CLEAR" or self._board2[x][y] == "CIRCLE":
                self._board2[x][y] = "BLACK"
            else:
                self._board2[x][y] = "CLEAR"

    def flag_at(self, x: int, y: int):
        if self._board2[x][y] == "CLEAR":
            self._board2[x][y] = "CIRCLE"

    def value_at(self, x: int, y: int) -> str:
        if 0 <= x < self._cols and 0 <= y < self._rows:
            if self._board2[x][y] == "BLACK":
                return str(self._board[x][y]) + '#'
            elif self._board2[x][y] == "CIRCLE":
                return str(self._board[x][y]) + "!"
        return str(self._board[x][y]) + ' '

    def finished(self) -> bool:
        for y in range(self._rows):
            for x in range(self._cols):
                val = self._board[x][y]
                if self._board2[x][y] != "BLACK":

                    for i in range(self._cols):
                        if self._board[x][i] == val and self._board2[x][i] != "BLACK":
                            return False
                    for i in range(self._rows):
                        if self._board[i][y] == val and self._board2[i][y] != "BLACK":
                            return False
                cont = 0
                confine = 0
                for dx, dy in ((0, 0), (0, -1), (1, 0),
                               (0, 1), (-1, 0)):
                    x1, y1 = x + dx, y + dy
                    if 0 <= x1 < self._cols and 0 <= y1 < self._rows:
                        if self._board2[x1][y1] == "BLACK":
                            cont += 1
                    else:
                        confine += 1
                    if cont + confine == 4:
                        return False
        return True

    def message(self) -> str:
        return "Puzzle solved!"
