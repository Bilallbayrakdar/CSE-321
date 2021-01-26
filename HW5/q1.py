
def isSubsetSum(arr, n, des):
	
	subset =([[False for i in range(des + 1)] 
			for i in range(n + 1)])
	
	for i in range(n + 1):
		subset[i][0] = True

	for i in range(1, des + 1):
		subset[0][i]= False

	for i in range(1, n + 1):
		for j in range(1, des + 1):
			if j<arr[i-1]:
				subset[i][j] = subset[i-1][j]
			if j>= arr[i-1]:
				subset[i][j] = (subset[i-1][j] or
								subset[i - 1][j-arr[i-1]])

	return subset[n][des]
		
if __name__=='__main__':
	arr = [2, 3, -5, -8, 6, -1]
	des = 0
	n = len(arr)
	if (isSubsetSum(arr, n, des) == True):
		print("Found a subset with given value")
	else:
		print("No subset with given value")
