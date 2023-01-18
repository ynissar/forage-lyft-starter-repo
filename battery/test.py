import unittest
from nubbinBattery import nubbinBattery
from spindlerBattery import splindlerBattery
from datetime import date

class TestEngine(unittest.TestCase):
    def testNubbinBatteryNeedsService(self):
        
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)
        
        nubbin = nubbinBattery(last_service_date,today)
        self.assertTrue(nubbin.needs_service())
    
    def testSpindlerBatteryNeedsService(self):
        
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        
        spindler = splindlerBattery(last_service_date,today)
        self.assertTrue(spindler.needs_service())




if __name__ == '__main__':
    unittest.main()
