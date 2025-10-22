#input a word or sentence
string=input("Enter your string: ")


string2=("")
for i in string:
    string2=i+string2


print("\nThe orignal string is:",string)
print("\nThe reversed string is :",string2)