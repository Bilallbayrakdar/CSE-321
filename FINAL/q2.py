# Python program for Quicksort
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
	i = ( low-1 )		 # index of smaller element 
	pivot = arr[high]	 # pivot 

	for j in range(low , high): 

		# If current element is smaller than or 
		# equal to pivot 
		if arr[j] <= pivot: 
		
			# increment index of smaller element 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arr,low,high): 
	if low < high: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(arr,low,high) 

		# Separately sort elements before 
		# partition and after partition 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
# print ("Sorted array is:") 
# for i in range(n): 
# 	print ("%d" %arr[i]), 

def Solve(A,Intervals):
	quickSort(A,0,len(A)-1)
    
	for i in Intervals:
		tmp = [A[i] for i in range(i[0],i[1])]
		print(tmp[0],"is the minimum of the [",i[0],",",i[1],"] interval.")

A = [7, 2, 3, 0, 5, 10, 11, 12, 18]
Intervals = [[0,4],[5,7], [7,8]]

# A = [1,2,3,4,5,6,2,8,10,9]
# Intervals  = [[0,4],[5,7]]



Solve(A,Intervals)