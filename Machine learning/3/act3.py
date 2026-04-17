def arraysum (a):
    total = 0
    for i in a:
        total += i
    return total

#examples
a = [12 , 3 , 4 , 15]
print('array sum: ',arraysum(a))