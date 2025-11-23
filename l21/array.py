import array as arr


#create an array
arrnum=arr.array('i',[1,3,5,3,7,3])
print("NUmber of occurance of the number 3 in the said array"+str(arrnum.count(3)))


#reverse the array
arrnum.reverse()
print("Reversed array is: ")
print(str(arrnum))