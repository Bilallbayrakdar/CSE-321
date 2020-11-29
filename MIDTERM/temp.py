def partition(arr, start, end): 
    pivot = arr[end] 
    print("pivot: ",pivot)
    i=j = start
    for i in range(start, end): 
        if arr[i] < pivot:
            print("i: ",a[i],"|| j: ",a[j])
            a[i], a[j]= a[j], a[i] 
            j+= 1
    print("j: ",a[j],"|| end:", a[end])
    a[j], a[end]= a[end], a[j] 
    return j 

def insertionSort(data, start, end): 
    for i in range(start + 1, end + 1):
        ele = data[i]
        j = i
        while j>start and data[j-1]>ele:
            print("data[j]: ",data[j], "|| data[j-1]: " ,data[j-1])
            data[j]= data[j-1]
            j-= 1
        data[j]= ele

a = [ 24, 97, 40, 67, 88, 85, 15, 
	66, 53, 44, 26, 48, 16, 52, 
	45, 23, 90, 18, 49, 80, 23 ] 

print(a,"\n") 


insertionSort(a,0,len(a)-1)

print(a) 




# data = reduc(data)
# # print(data)

# zeroMap = crtMap(data)
# # mxPrint(zeroMap)

# check(zeroMap)
# # mxPrint(zeroMap)

# sqrCheck(zeroMap)
# # mxPrint(zeroMap)


# data = mapToMx(zeroMap)
# # mxPrint(data)

# zeroMap = crtMap(data)
# check(zeroMap)
# # mxPrint(zeroMap)

# printResMap(zeroMap)