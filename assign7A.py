#program 7 -simple calculator
print("Select Operation!!")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.exit")
while(True):
    choice=int(input("enter your choice"))
    if choice in(1,2,3,4):
            num1=int(input("Enter first number:"))
            num2=int(input("Enter second number:"))
            if choice==1:
                print(num1,"+",num2,"=",num1+num2)
            elif choice==2:
                print(num1,"-",num2,"=",num1-num2)
            elif choice==3:
                print(num1,"*",num2,"=",num1*num2)
            elif choice==4:
                print(num1,"/",num2,"=",num1/num2)
    elif choice==5:
        break
    else:
        print("Invalid Input")
          




        
