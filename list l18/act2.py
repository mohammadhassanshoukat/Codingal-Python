#function to check wether
#first  and last characters of word match
def matchwords(words):
    ctr = 0
    lst=[]
    for word in words:
        if len(word)>1 and word[0] ==word[-1]:
            ctr+=1
            lst.append(word)

        print("list  of words with first  and last character same\n",lst)
        return ctr

count=matchwords(['abc', 'xyz', 'aba', '1221','cfc'])
print ("numbers of words  having first and last character same:",count)

