try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    result=num1/num2
    print("Result is:",result)
    print("result is",result1)

except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Please enter a numrical number")
except NameError as ex:
    print("The expection is ",ex)
    except:
    print("some error ocurred")
finally:
    print("I will execute no matter what happens")