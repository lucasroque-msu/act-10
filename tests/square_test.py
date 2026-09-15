import unittest 
from square import Square

class SquareTestCase(unittest.TestCase): 

    # pre-condition: a square instantiated with a negative side 
    # post-condition: the square's side is set to 1
    def testNegativeSide(self):
        square = Square(-1)
        self.assertEqual(1, square.side)

    # pre-condition: a square instantiated with side set to zero
    # post-condition: the square's side is set to 1
    def testZeroSide(self):
        square = Square(0)
        self.assertEqual(1, square.side)

    # pre-condition: a square instantiated with side set to 1
    # post-condition: the square's side is set to 1
    def testUnitarySide(self):
        square = Square(1)
        self.assertEqual(1, square.side)

    # pre-condition: a square instantiated with side set to 1
    # post-condition: the square's area is 1
    def testUnitarySideForArea(self):
        square = Square(1)
        self.assertEqual(1, square.area())

    # pre-condition: a square instantiated with side set to 1
    # post-condition: the square's perimeter is 4
    def testUnitarySideForPerimetyer(self):
        square = Square(1)
        self.assertEqual(4, square.perimeter())

    # pre-condition: a square instantiated with side set to 2
    # post-condition: the square's area is 4
    def testArbitrarySideForArea(self):
        square = Square(2)
        self.assertEqual(4, square.area())

    # pre-condition: a square instantiated with side set to 2
    # post-condition: the square's perimeter is 8
    def testArbitrarySideForPerimetyer(self):
        square = Square(2)
        self.assertEqual(8, square.perimeter())

if __name__ == '__main__':
    unittest.main(start_dir='src')