#removing elements from a dictionary

#create a dictionary
squares={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#remove a particular, returns its value
#output: 16
print(squares.pop(4))

#output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

#remove an arbitrary item, returns (key,value)
#output(5, 25)
print(squares.popitem())

#output: {1: 1, 2: 4, 3: 9}
print(squares)

#delete the dictionary itself
del squares


#throws error
print(squares)