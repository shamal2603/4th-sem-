def selectionSort(arr, size):
    for i in range(size):
        k=i
        for j in range (i+1, size):
            if arr[j] < arr[k]:
                k=j
        (arr[i], arr[k]) = (arr[k], arr[i])
arrsize = int(input("Enter the number of elements: "))
arr = []
for i in range(arrsize):
    arr.append(int(input("Enter the Elements: ")))
print("The array before sorting is :", arr)
selectionSort(arr, arrsize)
print("The array after sorting is : ", arr)
