from tire import Tire

class OctoprimeTires(Tire):
    def __init__(self, tireUsage):
        self.tireUsage = tireUsage

    def needs_service(self):
        sum = 0
        for x in self.tireUsage:
            sum += x
        if sum >= 3:
            return True
        else:
            return False