def minSumPath(A):
#storing the result in 1 D array
    dp = [None] * len(A)
    n = len(A) - 1
  
    # For the last row
    for i in range(len(A[n])):
        dp[i] = A[n][i]
  
    # Using dynamic approach in bottom up manner
    for i in range(len(A) - 2, -1,-1):
        for j in range( len(A[i])):
            dp[j] = A[i][j] + min(dp[j],dp[j + 1])
    # return the top element
    return dp[0]

# Calling the function
A = [
    [2],
   [5,4],
  [1,4,7],
 [8,6,9,6]
]

print(minSumPath(A))