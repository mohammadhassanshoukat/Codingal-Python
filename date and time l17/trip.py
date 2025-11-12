#define a function called hotel cost  with one argument nights as input
def hotel_cost(nights):
    return 140*nights
#define a function called palne ride cost that takes a string city as ,input
def plane_ride_cost(city):
    if "Chalotte"==city:
        return 183
    elif "Tampa"==city:
        return 220
    elif "Pittsburgh"==city:
        return 222
    elif "Los Angeles"==city:
        return 475
#define a function called car rental cost with an argument called days
def car_rental_cost(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40*days
# define a function called trip cost with an argument day, money and city
def trip_cost(city, days, spending_money):
    return hotel_cost(days)+plane_ride_cost(city)+car_rental_cost(days)+spending_money
print ("Cost of car rental: ", car_rental_cost(5)) 
print("Cost of plane ride: ", plane_ride_cost("Los Angeles"))
print("Cost of hotel room: ", hotel_cost(7))
print("Total trip cost: ", trip_cost("Los Angeles", 7, 500))
print(trip_cost("Tampa", 6,500))