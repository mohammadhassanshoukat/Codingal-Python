def firstsetbit (n):

    #count variable set as 0

    count = 0

    #right shift the number until we find the first set bit 

    while(n):

        if (n&1==1):


            break

        count +=1 

        n >>= 1
        
    
    return count