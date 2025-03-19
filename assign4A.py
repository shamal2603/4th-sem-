num=int(input("enter a number:"))
if num<=0:
    print("enter a positive number:")
else:    
    print("Multipliction table of",num)
    for i in range(1,11,1):
        print(num,"X",i,"=",(num*i))
