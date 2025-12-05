# create int method
class vehicle:

    #create init method
    def __init__(self,max_speed, mileage):
        vehicle.max_speed = max_speed
        vehicle.mileage = mileage

# create object
car = vehicle(240, 18)

#access the variables inside init method
print("Max Speed:", car.max_speed)
print(" Model Mileage:", car.mileage)