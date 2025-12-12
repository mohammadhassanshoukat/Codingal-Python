class vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class Bus(vehicle):
    pass

schoolbus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", schoolbus.name, "Speed:", schoolbus.maxspeed, "Mileage:", schoolbus.mileage)