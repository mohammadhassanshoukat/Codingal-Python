#define function to calculate cube 
def cube(number):
    return number*number*number

#define a function which will execute cube function if the user enter umber is divisibled by 3
def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False

#display result 
print(by_three(27) )#output 729
print(by_three(19)) #output false