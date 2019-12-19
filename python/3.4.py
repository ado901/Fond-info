class Meteo:
    def __init__(self, nome: str):
        self._nome = nome
        self._piovosità = []

    def aggiungi(self, dati):
        self._piovosità.append(dati)

    def tot(self, dato1, dato2):
        data1 = None
        data2 = None
        for i in self._piovosità:
            a = dato1
            b, c = i
            if a == b:
                data1 = c
        for i in self._piovosità:
            a = dato2
            b, c = i
            if a == b:
                data2 = c

        return data1 + data2


def main():
    a = str(input("inserire data: "))
    b = float(input("inserire mm pioggia: "))
    met = Meteo("Aeronautica Militare")
    while b >= 0:
        met.aggiungi((a, b))
        a = str(input("inserire data: "))
        b = float(input("inserire mm pioggia: "))
    while True:
        a = input("data 1: ")
        b = input("data 2: ")
        print(met.tot(a, b))


if __name__ == '__main__':
    main()
