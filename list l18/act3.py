l=[4,5,1,2,9,7,10,8]
print("original list:",l)

#variable to store the sum
# of list 
count=0
#finding the sum
for i in l:
    count+=i


#diveide the total elements by
#number of elements
avg=count/len(l)
print("sum = ",count)
print("average = ",avg)

#sorting the elements of the list 
l.sort()


#print the first element
print("smallest element =",l[0])

#print the last element
print("largest element =",l[-1])