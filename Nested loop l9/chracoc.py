#take input of a word
string=input("lease enter your own word")
#take input off a chracter
char=input("please enter your own character")
i=0
count=0
#loop will find the occurance of the character
while(i<len(string)):

    if(string[i]==char): #condition 1
        count=count+1
    i=i+1


#display the result
print("total number of times ",char,"has occured =",count)