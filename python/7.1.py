from Actor import *
import unittest


class MyTest(unittest.TestCase):

    def testsfondo(self):
        arena = Arena(500, 600)
        sfondo = Sfondo(arena, (0, 500, 500, 100), (100, 500, 200, 300), -1)

        self.assertEqual(sfondo.symbol(), (100, 500, 200, 300))
        self.assertEqual(sfondo.position(), (0, 500, 500, 100))

    def testrover(self):
        arena = Arena(500, 600)
        rover = Rover(arena, 100, 500)
        self.assertEqual(rover.position(), (100, 500, 31, 23))


if __name__ == '__main__':
    unittest.main()
