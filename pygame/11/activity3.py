#program to deleted lines from a file

#creating the output file
outputfile = open('UpdatedFile.txt','w')

#reading the input file
inputfile = open('Repeated.txt',"r")

#holds lines already seen
lineseensofar = set()
print("Eleminitating duplicated lines which were in the file...... ")
#litering every line in the file
for line in inputfile:

    #checking if line is unique
    if line not in lineseensofar:


        #write lines in output file
        outputfile.write(line)


        #add unique lines to lineseensofar
        lineseensofar.add(line)

#closing the files
inputfile.close()
outputfile.close()