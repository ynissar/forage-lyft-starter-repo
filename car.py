from serviceable import serviceable

class Car(serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        if self.engine.needs_service() and self.battery.needs_service():
            return True
        else:
            return False