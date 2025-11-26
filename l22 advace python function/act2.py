#zipelemnts of two lists
s1=[2,3,1]
s2=['b','c','a']
s3=list(zip(s1,s2))
print(s3,"\n")


#zip of two elements
#print elements by one by one, but elemnts of second list will be inreverse order
l1=[10,20,30,40]
l2=[100,200,300,400]

for x,y in zip(l1,l2[::-1]):
    print(x,y)

#zip into dictionary
stocks=['reliance','infosys','tcs']
prices=[2175,1127,2750]


new_dict={stocks: prices for stocks,
           prices in zip(stocks,prices)}
print('\n{}'.format(new_dict))