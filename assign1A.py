#fibonacci sequence
n=int(input("Enter the number:"))
c=0
a=0
b=1
if n==0 or n==1:
    print("Yes it belongs to Fibonacci Sequence")
else:
    while c<n:
        c=a+b
        b=a
        a=c
if c==n:
    print("Yes it belongs to Fibonacci Sequence")
else:
    print("No it does not belongs to Fibonacci Sequence")
            
        
