import unittest
from capulet_engine import CapuletEngine
from sternman_engine import SternmanEngine
from willoughby_engine import WilloughbyEngine

class TestEngine(unittest.TestCase):
    def testCapuletEngineNeedsService(self):
        currentMileage = 30101
        last_service_mileage = 100

        capulet = CapuletEngine(currentMileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())

    def testWilloughbyEngineNeedsService(self):
        currentMileage = 60101
        last_service_mileage = 100

        willoughy = WilloughbyEngine(currentMileage, last_service_mileage)
        self.assertTrue(willoughy.needs_service())
        
    def testSternmanEngineNeedsService(self):
        warningLight = True

        sternman = SternmanEngine(warningLight)
        self.assertTrue(sternman.needs_service())


if __name__ == '__main__':
    unittest.main()
