#creation of class
class myclass:

    #private variable
    _privatevar=27;

    #creation of private method
    def _privmeth(self):
        print("I'm inside class myclass")

    #function to print value of private variable
    def hello(self):
        print("The value of private variable is:",self._privatevar)
        
#creation of object
foo=myclass()
foo.hello()
foo.privmeth()  #accessing private method outside the class