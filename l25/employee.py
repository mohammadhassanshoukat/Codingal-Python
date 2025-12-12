#create class
class Employee:
    #initializing
    def __init__(self):
        print("employee created")

        #calling distructor
    def __del__(self):
        print("destructor called, employee deleted")

def create_obj():
    print("making object...")
    obj = Employee()
    print("function end")
    return obj

print("calling create_obj() function")
obj=create_obj()
print("program end")