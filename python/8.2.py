import os


def cifre(testo):
    count = 0
    testo = testo.strip()
    testo = testo.strip(" ")
    for i in testo:
        try:
            if 0 <= int(i) <= 9:
                count += 1
        except ValueError:
            pass
    print(count, len(testo))
    return (count / len(testo)) * 100


def main():
    if os.path.isfile("boh.txt"):
        with open("boh.txt", "r") as myfile:
            testo = ""
            for indice, riga in enumerate(myfile):
                print("percentuale caratteri alla riga", indice, ": ", cifre(riga))
                testo += riga
            print("percentuale cifre del testo: ", cifre(testo))
    else:
        print("Non esiste file")


if __name__ == '__main__':
    main()
