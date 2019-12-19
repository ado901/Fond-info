class Box:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def perimeter(self) -> float:
        return self._width * 2 + self._height * 2

    def area(self) -> float:
        return self._height * self._width


def main():
    width = float(input("inserire width "))
    height = float(input("inserire height "))
    box = Box(width, height)
    print("area: ", box.area(), "perimeter: ", box.perimeter())


if __name__ == '__main__':
    main()
