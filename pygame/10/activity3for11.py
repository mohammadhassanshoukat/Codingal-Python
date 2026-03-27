#program to remove lines startung with prefix
file1 = open('Codingal.txt','r')
file2 = open('CodingalUpdate.txt','w')


#reading each line from orignal
#text file
for line in file1.readlines():

    #reading all lines that do not
    #brgin with "coding"
    if not 