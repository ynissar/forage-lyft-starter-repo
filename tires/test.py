import unittest
from carrigan_tires import CarriganTires
from octoprime_tires import OctoprimeTires

class tiresTest(unittest.TestCase):
    def testCarriganTiresNeedsService(self):
        tireUsage = [0, 1, 0, 0]
        tires = CarriganTires(tireUsage)

        self.assertTrue(tires.needs_service())

    def testOctoprimeTiresNeedsService(self):
        tireUsage = [0, 1, 1, 1]
        tires = OctoprimeTires(tireUsage)

        self.assertTrue(tires.needs_service())
    

if __name__ == '__main__':
    unittest.main()