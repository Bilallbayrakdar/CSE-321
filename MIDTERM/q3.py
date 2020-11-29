# Python implementation of the above approach 

# Function to make insertion sort
def insertionSort(data, start, end): 
	for i in range(start + 1, end + 1): 
		ele = data[i] 
		j = i 
		while j>start and data[j-1]>ele: 
			data[j]= data[j-1] 
			j-= 1
		data[j]= ele 



# Partition function which gets 
# start and end index of the list 
# then it returns the index of the pivot
def partition(arr, start, end): 
	pivot = arr[end] 
	i = j = start 
	for i in range(start, end): 
		if arr[i]<pivot: 
			a[i], a[j]= a[j], a[i] 
			j+= 1
	a[j], a[end]= a[end], a[j] 
	return j 

# Sorts elements of the given array which's 
# index are between start and end
def quickSort(arr, start, end): 
	if start<end: 
		pivot = partition(arr, start, end) 
		quickSort(arr, start, pivot-1) 
		quickSort(arr, pivot + 1, end) 
		return arr 

# This function sort the number which are between 
# start and end index. It's sorting approach is 
# using insertion sort for small arrays and using 
# quick sort for larger arrays. To entitle an 
# array small I determined an treshold which is 10. 
# If array's lenght is smaller or equal to the 10 
# it small or if it is bigger it is large 
def hybrid_quickSort(arr, start, end): 
	while start<end: 

		# If the length of the array is less 
		# than threshold I call insertion sort 
		if end-start + 1<10: 
			insertionSort(arr, start, end) 
			break

		else: 
			pivot = partition(arr, start, end) 

			# Optimised quicksort which works on 
			# the smaller arrays first 

			# If the left side of the pivot 
			# is less than right, sort left part 
			# and move to the right part of the array 
			print()
			print("pivot: ",pivot)
			print("start: ",start)
			print("end: ", end)
			print("pivot-start: ",pivot-start,"end-pivot: ",end-pivot)
			if pivot-start<end-pivot: 
				print("case1")
				hybrid_quickSort(arr, start, pivot-1) 
				start = pivot + 1
			else: 
				print("case2")
				# If the right side of pivot is less 
				# than left, sort right side and 
				# move to the left side 
				hybrid_quickSort(arr, pivot + 1, end) 
				end = pivot-1

# Driver code 

a = [ 
	24, 97, 40, 67, 88, 85, 15, 
	66, 53, 44, 26, 48, 16, 52, 
	45, 23, 90, 18, 49, 80, 23 ] 
hybrid_quickSort(a, 0, 20) 
print(a) 
