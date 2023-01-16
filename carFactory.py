from car import Car
from engine import capulet_engine, sternman_engine,willoughby_engine
from battery import nubbinBattery, spindlerBattery

@staticmethod
def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = capulet_engine(current_mileage, last_service_mileage)
    battery = spindlerBattery(current_date, last_service_date)

    return Car(engine, battery)

@staticmethod
def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = willoughby_engine(current_mileage, last_service_mileage)
    battery = spindlerBattery(current_date, last_service_date)

    return Car(engine, battery)

@staticmethod
def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = sternman_engine(current_mileage, last_service_mileage)
    battery = spindlerBattery(current_date, last_service_date)

    return Car(engine, battery)

@staticmethod
def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = willoughby_engine(current_mileage, last_service_mileage)
    battery = nubbinBattery(current_date, last_service_date)

    return Car(engine, battery)

@staticmethod
def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = capulet_engine(current_mileage, last_service_mileage)
    battery = nubbinBattery(current_date, last_service_date)

    return Car(engine, battery)
