try:
    num=int(input("ENter a number: "))
    print(num)
except ValueError as ex:
    print("expection",ex)


print("i am outside the try bock")