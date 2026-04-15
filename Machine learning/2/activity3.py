def CNSquaretime(n):
    iteration=0
    for i in range (0,n):
        for j in range (0,n):
            print('*',end=' ')
            iteration+=1
        print('')
    print('\nWhen n is ',n,'iterations = ',iteration,'\n')


CNSquaretime(5)
CNSquaretime(4)
CNSquaretime(3)


print('\n with every n the time will increase by n^2')
print('O(n^2)')