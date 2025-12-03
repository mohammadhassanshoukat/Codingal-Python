#add two list using map and lambda function
numbers1=[1,2,3]
numbers2=[4,5,6]
result=map(lambda x,y:x+y,numbers1,numbers2)
print("Addiotion of 2 list")
print(list(result))


#using map
nums=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq,nums))
print("\n ")
print("Square of square of numbers in list")
print(square)