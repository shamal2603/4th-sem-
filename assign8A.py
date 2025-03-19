#Assignment 8-string operations
print("---Menu---")
print("1.String Swap case")
print("2.String Length")
print("3.String Uppercase")
print("4.String lowercase")
print("5.String Indexing")
print("6.String Slicing")
print("7.Exit")

while(True):
    i=int(input("Enter your Choice: "))
    if i==1:
        s1=input("Enter String: ")
        print("String Swap case ",s1.swapcase())
    elif i==2:
        s1=input("Enter String to find its lenght: ")
        print("Length of string is ",len(s1))
    elif i==3:
        s1=input("Enter String in lowercase: ")
        print("Upper of string is",s1.upper())
    elif i==4:
        s1=input("Enter String in Uppercase: ")
        print("Lowercase of string is",s1.lower())
    elif i==5:
        s1=input("Enter String for Indexing: ")
        pos=int(input("Enter position to extract"))
        print("Character at position",pos, "is", s1[pos-1])
    elif i==6:
        s1=input("Enter String for slicing: ")
        start=int(input("Enter starting position to extract: "))
        end=int(input("Enter ending position of exstract: "))
        print("Sliced String is",s1[start:end])
    elif i==7:
        break
    else:
        print("Invalid Choice")

    
