from tire import Tire

class CarriganTires(Tire):
    def __init__(self, tireUsage):
        self.tireUsage = tireUsage

    def needs_service(self):
        for x in self.tireUsage:
            if x >= 0.9:
                return True
        return False