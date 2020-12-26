import numpy
# Partition function which gets 
# start and end index of the list 
# then it returns the index of the pivot
def partition(arr, start, end): 
    pivot = arr[end] 
    i = j = start 
    swAmount = 0
    
    for i in range(start, end): 
    	if arr[i]<pivot: 
            swAmount += 1
            arr[i], arr[j]= arr[j], arr[i] 
            j+= 1
    swAmount += 1
    arr[j], arr[end]= arr[end], arr[j]
    return (int(j),swAmount)  

# Sorts elements of the given array which's 
# index are between start and end
def quickSortBody(arr, start, end):
    swAmount = 0 
    if start<end: 
        pivot = partition(arr, start, end) 
        swAmount+= pivot[1]
        quickSortBody(arr, start, pivot[0]-1) 
        quickSortBody(arr, pivot[0] + 1, end)
        
    return swAmount

def quickSort(arr):
    return quickSortBody(arr, 0, len(arr)-1)

def insertionSort(arr): 
    swAmount = 0
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                swAmount +=1
                # print(swAmount)
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
        # swAmount+=1
    return swAmount 

print("10----------------------------------")
arr_2 = numpy.ndarray([10])
arr_1 = numpy.random.randint(10, size=(10))
numpy.copyto(arr_2,arr_1)
print(quickSort(arr_1))
print(insertionSort(arr_2))
print("100----------------------------------")
arr_2 = numpy.ndarray([100])
arr_1 = numpy.random.randint(100, size=(100))
numpy.copyto(arr_2,arr_1)
print(quickSort(arr_1))
print(insertionSort(arr_2))
print("1000----------------------------------")
arr_2 = numpy.ndarray([1000])
arr_1 = numpy.random.randint(1000, size=(1000))
numpy.copyto(arr_2,arr_1)
print(quickSort(arr_1))
print(insertionSort(arr_2))
print("10000----------------------------------")
arr_2 = numpy.ndarray([10000])
arr_1 = numpy.random.randint(10000, size=(10000))
numpy.copyto(arr_2,arr_1)
print(quickSort(arr_1))
print(insertionSort(arr_2))
print("100000----------------------------------")
# arr_2 = numpy.ndarray([10000])
# arr_1 = numpy.random.randint(100000, size=(100000))
# numpy.copyto(arr_2,arr_1)
# print(quickSort(arr_1))
# print(insertionSort(arr_2))
# print("----------------------------------")