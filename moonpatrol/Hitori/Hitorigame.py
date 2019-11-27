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
    def __init__(self, side=8, level=4):
        self._cols, self._rows = side, side
        self._board = []
        with open("matrice.txt") as myfile:
            for i in myfile:
                i = i.strip()
                self._board.append(i.split(","))

        # self._board = [[random.randint(1, 9) for y in range(side)] for x in range(side)]
        self._board2 = [["CLEAR" for y in range(side)] for x in range(side)]

    def cols(self) -> int:
        return self._cols

    def rows(self) -> int:
        return self._rows

    def play_at(self, x: int, y: int):
        if 0 <= x < self._cols and 0 <= y < self._rows:
            if self._board2[y][x] == "CLEAR" or self._board2[y][x] == "CIRCLE":
                self._board2[y][x] = "BLACK"
            else:
                self._board2[y][x] = "CLEAR"
            for i in self._board2:
                print(i)
            print()

    def flag_at(self, x: int, y: int):
        if self._board2[y][x] == "CLEAR":
            self._board2[y][x] = "CIRCLE"

    def value_at(self, x: int, y: int) -> str:
        if 0 <= x < self._cols and 0 <= y < self._rows:
            if self._board2[y][x] == "BLACK":
                return str(self._board[y][x]) + '#'
            elif self._board2[y][x] == "CIRCLE":
                return str(self._board[y][x]) + "!"
        return str(self._board[y][x]) + ' '

    def checkcontinuity(self, y, x, matrice):
        count = 1
        print(self._board[y][x], end=' ')
        for dx, dy in ((0, -1), (1, 0),
                       (0, 1), (-1, 0)):
            x1, y1= x+dx, y+dy
            if 0 <= x1 < self._cols and 0 <= y1 < self._rows:

                if self._board2[y1][x1] != "BLACK" and not matrice[y1][x1]:
                    print(self._board[y1][x1], y1, x1)
                    matrice[y1][x1] = True
                    count += self.checkcontinuity(y1, x1, matrice)
        return count

    def finished(self) -> bool:
        totale=0
        for y in range(self._rows):
            for x in range(self._cols):
                val = self._board[y][x]
                if self._board2[y][x] != "BLACK":
                    totale+=1
                    for i in range(self._cols):
                        if i != x and self._board[y][i] == val and self._board2[y][i] != "BLACK":
                            return False
                    for i in range(self._rows):

                        if i != y and self._board[i][x] == val and self._board2[i][x] != "BLACK":
                            return False

                if self._board2[y][x] == "BLACK":
                    for dx, dy in ((0, -1), (1, 0),
                                   (0, 1), (-1, 0)):
                        if 0 <= x + dx < self._cols and 0 <= y + dy < self._rows:
                            if self._board2[y + dy][x + dx] == "BLACK":
                                return False
        matrice = [[False for y in range(self._cols)] for x in range(self._rows)]
        tmp = 0
        while True:
            if self._board2[0][tmp] != "BLACK":
                matrice[0][tmp] = True
                tot = self.checkcontinuity(0, tmp, matrice)
                print(tot, totale)
                break
            tmp += 1
        if tot!=totale:
            return False

        return True

    def message(self) -> str:
        return "Puzzle solved!"
