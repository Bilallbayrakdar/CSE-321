#%%
from self_balancing_binary_search_tree import SBBST

nums = [1,2,3,6,5,4] # random numbers

#%%
"""
This function's complexity is O(nlogn). If we dive in findPair 
function we can see that :

    1-  The first line of this function defines
        a new SBBST which's complexity is O(1) time.
    2-  Then we see a for loop which iterates over 
        arr. This one is O(n) operation.
    3-  Inside for loop function checks that the
        remainder of the desired number after modulo 
        operation by current element of the array whether
        equals zero or not. This one is O(n) too.
    4-  When if statement in the 3rd part has true as an
        input, function searches target inside SBBST.
        It is O(logn) time operation.
    5-  If SBBST has target function prints the pair.
        This operation is O(1) time.
    6-  Else function inserts current element of the array
        into SBBST. This operation is O(logn).

To sum up, since after 2nd state all operations happens
inside for loop O(n) comes from this linear iteration.
Then O(logn) comes from "search or insert" case. (Since 
one of them has to be happen).

Complexity of this function : O(nlogn)

"""
#%%

def findPair (arr, des):
    ST = SBBST()
        
    for ele in arr: 
        if (des%ele ==0):
            target = int(des/ele)
            if ST.search(ST.head,target):
                print("({},{})".format(ele,target))
            else:
                ST.insert(ele)
#%%
ST = SBBST()

arr= [-2,-4,2,4,1]
findPair(arr,8)