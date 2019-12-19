def function(parola: str) -> float:
    i = 0
    k = 0
    for a in parola:
        print("lettera: ", a)
        if "A" <= a <= "Z":
            k += 1
        i += 1
    print("k: ", k, "i: ", i)
    return k / i * 100


def main():
    parola = input("digitare una parola:")
    print("il rapporto delle lettere maiuscole sul totale è", function(parola), "%")


if __name__ == '__main__':
    main()
