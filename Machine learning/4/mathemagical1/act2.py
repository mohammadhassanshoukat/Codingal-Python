#find thr factor of a njumber given by the user

#goes from 1 to number and checks  if i divides the number if yes it is factor
def printfactors (num):
    print('the factors of',num,'are: ')
    for i in range(1,num+1):
        if num%i ==0:
            print(i)

#taking inpit from the user
num = int(input('Enter the number of which you want to find the factor of: '))

#calling our functions
printfactors(num)