def pow(n: int, el: int):
    if el == 0:
        return 1
    else:
        return n * pow(n, el - 1)


def main():
    n = int(input("numero?"))
    el = int(input("potenza?"))
    print(pow(n, el))


if __name__ == '__main__':
    main()
