#create a tuplet with different data types
tuplex=("tuple", False, 3.2, 1)
print(tuplex)

#create a tuplet
tuplex=(4, 6, 2, 8, 3, 1)
print(tuplex)
#tuplets are immutable, so you cannot add new elements
#using merge of tuples with the + operator you can add an element  and it will create a new tuple
tuplex=tuplex+(9,)
print(tuplex)

#counts the number of occurrences of an element in a tuplet
tuple1=(50,10,60,70,50)
print(tuple1.count(50))

#create a tuple
tuplex=(2, 4, 3, 5, 4, 6, 7, 8, 6, 1 )
_slice=tuplex[3:5]
print(_slice)


_slice=tuplex[:6]
print(_slice)