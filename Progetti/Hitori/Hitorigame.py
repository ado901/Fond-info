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
    def __init__(self, size):

        self._board = []
        with open("matrice" + size + ".txt") as myfile:
            righe = 0
            for i in myfile:
                righe += 1
                i = i.strip()
                self._board.append(i.split(","))
            self._cols, self._rows = int(size), int(size)

        # self._board = [[random.randint(1, 9) for y in range(side)] for x in range(side)]
        self._board2 = [["CLEAR" for y in range(int(size))] for x in range(int(size))]

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

    def checkcontinuity(self, y, x, matrice=None):
        if matrice == None:
            matrice = [[False for y in range(self._cols)] for x in
                       range(self._rows)]
        matrice[y][x] = True
        count = 1  # in partenza il contatore sicuramente è 1 per entrare nella funzione
        for dx, dy in ((0, -1), (1, 0),
                       (0, 1), (-1, 0)):
            x1, y1 = x + dx, y + dy
            if 0 <= x1 < self._cols and 0 <= y1 < self._rows:

                if self._board2[y1][x1] != "BLACK" and not matrice[y1][x1]:  # se la matrice adiacente a quella di partenza è bianca e non è stata ancora controllata
                    matrice[y1][x1] = True
                    count += self.checkcontinuity(y1, x1,matrice)  # controllo tramite ricorsione anche quella adiacente e lo metto nel contatore
        return count

    def circle(self):
        for y in range(self._rows):
            for x in range(self._cols):
                if self._board2[y][x] == "BLACK":
                    for dx, dy in ((0, -1), (1, 0),
                                   (0, 1), (-1, 0)):
                        x1, y1 = x + dx, y + dy
                        if 0 <= x1 < self._cols and 0 <= y1 < self._rows:
                            if self._board2[y1][x1] == "CLEAR":
                                self._board2[y1][x1] = "CIRCLE"
                            elif self._board2[y1][x1] == "CIRCLE":
                                self._board2[y1][x1] = "CLEAR"

    def black(self):
        for y in range(self._rows):
            for x in range(self._cols):

                if self._board2[y][
                    x] == "CIRCLE":  # se trovo cella non annerita controllo che nelle righe e nella colonna non ci sia lo stesso numero
                    val = self._board[y][x]
                    for i in range(self._cols):
                        if i != x and self._board[y][i] == val and self._board2[y][i] == "CLEAR":
                            self._board2[y][i] = "BLACK"
                    for i in range(self._rows):
                        if i != y and self._board[i][x] == val and self._board2[i][x] == "CLEAR":
                            self._board2[i][x] = "BLACK"

    def countbianchi(self) -> int:
        count = 0
        for y in range(self._rows):
            for x in range(self._cols):
                if 0 <= y < self._rows and 0 <= x < self._cols:
                    if self._board2[y][x] != "BLACK":
                        count += 1
        return count

    def solve_recursive(self, i,u):
        if 0<= i < self._rows and 0<= u < self._cols:
            for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
                x1, y1 = x+dx, y+dy
                if 0<= x1 < self._rows and 0<= y1 < self._cols:


    def wrong(self) -> list:
        errore = []
        listablack = []
        listacircle = []

        for y in range(self._cols):
            for x in range(self._rows):
                if self._board2[y][x] == "BLACK":

                    for dx, dy in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                        x1, y1 = x + dx, y + dy
                        if 0 <= x1 < self._rows and 0 <= y1 < self._cols and (y, x) not in listablack:
                            if self._board2[y1][x1] == "BLACK":
                                errore.append("Cella nera a posizione " + str(y) + str(
                                    x) + " contigua con cella a posizione " + str(y1) +
                                              str(x1))
                                listablack.append((y1, x1))
                if self._board2[y][x] == "CIRCLE":
                    val = self._board[y][x]
                    for i in range(self._cols):
                        if i != x and self._board[y][i] == val and self._board2[y][i] == "CIRCLE" and (
                                y, x) not in listacircle:
                            errore.append(
                                "Cella cerchiata a posizione " + str(y) + " " + str(x) + " con valore " + val +
                                " allineata con cella cerchiata a posizione " + str(y) + " " + str(
                                    i) + " con valore " + str(self._board[y][i]))
                            listacircle.append((y, i))
                    for i in range(self._rows):
                        if i != y and self._board[i][x] == val and self._board2[i][x] == "CIRCLE" and (
                                y, x) not in listacircle:
                            errore.append(
                                "Cella cerchiata a posizione " + str(y) + " " + str(x) + " con valore " + val +
                                " allineata con cella cerchiata a posizione " + str(i) + " " + str(
                                    x) + " con valore " + str(self._board[i][x]))
                            listacircle.append((i, x))
        tmp = 0
        boolean = False
        while not boolean:  # Controllo prima cella che trovo bianca
            if self._board2[0][tmp] != "BLACK":
                boolean = True
                tot = self.checkcontinuity(0, tmp)
            tmp += 1
        if tot != self.countbianchi():
            errore.append("Celle bianche non contigue")
        return errore

    def finished(self) -> bool:
        for i in self._board2:
            print(i)
        print()
        totale = self.countbianchi()

        for y in range(self._rows):
            for x in range(self._cols):
                val = self._board[y][x]
                if self._board2[y][
                    x] != "BLACK":  # se trovo cella non annerita controllo che nelle righe e nella colonna non ci sia lo stesso numero
                    for i in range(self._cols):
                        if i != x and self._board[y][i] == val and self._board2[y][i] != "BLACK":
                            return False
                    for i in range(self._rows):
                        if i != y and self._board[i][x] == val and self._board2[i][x] != "BLACK":
                            return False

                if self._board2[y][x] == "BLACK":  # controllo che le celle annerite non siano adiacenti
                    for dx, dy in ((0, -1), (1, 0),
                                   (0, 1), (-1, 0)):
                        if 0 <= x + dx < self._cols and 0 <= y + dy < self._rows:
                            if self._board2[y + dy][x + dx] == "BLACK":
                                return False

        tmp = 0
        boolean = False
        while not boolean:  # Controllo prima cella che trovo bianca
            if self._board2[0][tmp] != "BLACK":
                boolean = True
                tot = self.checkcontinuity(0, tmp)
                print(tot, totale)
            tmp += 1
        if tot != totale:
            return False

        return True

    def message(self) -> str:
        return "Puzzle solved!"
