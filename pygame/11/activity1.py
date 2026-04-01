#write in file using ( ) function
with open ('Codingal.txt', 'w') as file:
    file.write('I am penguin and i am 1 years old')
file.close()

#split files into seperated words
with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in file are: \n")
    for line in data:
        word = line.split()
        print (word)
file.close()