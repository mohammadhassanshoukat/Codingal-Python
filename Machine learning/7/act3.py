#proggram to find the number of bits present in a number
#functions taking our number as input
def numberofbits(n):
    #count varible set as 0
    count = 0
    #right shift the number till it becomes 0
    while (n):
        count += 1
        n >>= 1
    return count
num = int(input('Enter a number: '))
print('Number of bits in', num, 'is', numberofbits(num))