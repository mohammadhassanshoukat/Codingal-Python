#program to check if the nit bit is set or not 

def setornot (number, n):

    #make a mask variable by left shifting 1 (k+1) time and check if (n AND mask) equals 1 or 0 
    if number & (1 << (n - 1)):

        print('\n SET')

    else:
        print('\n NOT SET')


number = int(input ('enter your number : '))
n = int(input ('Enter a bit number for this python prgram to check: '))
setornot (number, n)