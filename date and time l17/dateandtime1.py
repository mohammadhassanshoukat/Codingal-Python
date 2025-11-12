from datetime import date , time , datetime

#calling today
# function of day class
today = date.today()
now = datetime.now()
print("Today's date: ", today)
print("\nCurrent time and date is: ", now)

#printing dates components
print("\nDate components: ", today.year, today.month, today.day)



