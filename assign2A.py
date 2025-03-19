#Assignment2
#Solve Quadratic Equations and print the roots
import math
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
# If a is 0,then incorrect equation
if a==0:
    print("Incorrect input ,quadratic equation not possible")
else:
    # calculating discriminant using formula
    dis= b * b - 4 * a * c
    numer=math.sqrt(abs(dis))
    den=2 * a
    # cheking condition for discriminant
    if dis>0:
         print(" real and differnt roots")
         print((-b+numer)/(den))
         print((-b-numer)/(den))
    elif dis==0:
        print("real and same roots")
        print(-b/(den))
    # when discriminant is less than 0
    else:
        print("complex roots or imaginary roots")
        print(-b/(den),"+i",numer) 
        print(-b/(den),"-i",numer)
