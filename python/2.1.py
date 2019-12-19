def cels_to_fahr(a: float) -> float:
    return a * 1.8 + 32


def main():
    a = float(input("inserire grado celsius: "))
    print(cels_to_fahr(a))


if __name__ == '__main__':
    main()
