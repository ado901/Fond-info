from HitoriGui import BoardGameGui, gui_play
from Hitorigame import HitoriGame


def main():
    size = input("Size? (8x8, 10x10)")
    if size == "8" or size == "8x8":
        size = "8"
    elif size == "10" or size == "10x10":
        size = "10"
    gui_play(size)


if __name__ == '__main__':
    main()
