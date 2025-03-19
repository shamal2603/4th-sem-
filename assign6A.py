#assighnment 6:implement a sequential search using list

def sequential_Search(list1,n,key):
    for i in range(0,n):
        if (list1[i]==key):
            return i
    return -1

n=int(input("enter size of n:"))
print(f"enter {n} elements:")
list1=[]
for i in range(0,n):
    list1.append(int(input()))
print("Given list is",list1)
key=int(input("enter an element you wish to search from a list:"))
n=len(list1)
res=sequential_Search(list1,n,key)
if(res==-1):
    print("Element not found")
else:
   print("Element found at index:",res) 
