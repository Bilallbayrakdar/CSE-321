#%%
"""
I used set in my implementation. Because python uses HashSet and in the Hash Set structure every number has specific hash value. 
And getting this hash value is O(1) time operation. Because generally hashed value is produced with the help of a constant prime 
number and modulo.(I also checked my axiom from here: https://www.jessicayung.com/how-python-implements-dictionaries/) And a Hash 
Set holds all of its element as like multi dimensional array (which referred as "table" in many documents: 
https://www.laurentluce.com/posts/python-dictionary-implementation/) of hashed values, so getting an element is O(1) time if you 
know the desired element.  Since there is an array in hash sets and elements are placed according to their hash values, there could 
be collisions but python uses probing to overcome this situation and also it increments the vertical size of the array. As a result 
using Set gives opportunity use add and get operations in O(1) time*.

At first function converts the large array to the python set. This is O(n) time operation. After that function iterates over small 
array and checks whether the set which is produced from large array  has the current element of the small array or not. This is an 
O(1) time operation because  according to python documents the Set is implemented by using HashSet. If set has current  element, 
function appends the current element into the result list. Also this one is O(1) time  complex.

To sum up there is a for loop which O(n) and there is an other for loop which also O(n) and second for loop has two sub-operations 
inside. Both of them are O(1) time operations. So this function has O(n) time complexity.
	• Note : I used python's doc's for my axioms : https://wiki.python.org/moin/TimeComplexity

"""
#%%
def findCommon(bArr, sArr):
    temp = set()
    res = list()
    for ele in bArr:
        temp.add(ele)
    for ele in sArr:
        if(ele in temp):
            res.append(ele)
    return res

#%%
arr1 = [1,2,3,4,5,6,7]
arr2 = [1,2,3]

print(findCommon(arr1,arr2))