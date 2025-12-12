#create a class
class IOSstring():

    #constructor to set defualt value
    def __init__(self):
        self.string = ""

    #function to get input from user
    def getString(self):
        self.string = input("Enter a string: ")
    
    #function to print the string in uppercase
    def printString(self):
        print(self.string.upper())

#object creation
str1 = IOSstring()

#calling functions
str1.getString()
str1.printString()