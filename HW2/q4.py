# binary tree node 
class Node: 
    def __init__(self, d): 
        self.data = d 
        self.left = None
        self.right = None

"""
This method converts a binary tree to a list in inrder traversal order
"""
def storeInorder(node, inorder):
    if node == None:
        return
    # first go left part
    storeInorder(node.left, inorder)
    # add to the array
    inorder.append(node.left.data)
    # then go right part
    storeInorder(node.right, inorder)

"""
This method merges two sorted list 
in ascending order. Returns the the 
merged list.

m: lenght of the list1
k: lenght of the list2
"""
def merge(list1, list2, m, k):

    i=0
    j=0
    res = list()

    while i<m and j<k:
        if list1[i] < list2[j]:
            res.append(list1[i])
            i+=1
        else:
            res.append(list2[j])
            j+=1

    while i<m:
        res.append(list1[i])
        i+=1
    
    while j<k:
        res.append(list2[j])
        j+=1
    
    return res

def sortedListToBST(aList, i, j):
    if(i > j):
        return None
    
    middle = (i+j)/2
    head = Node(aList[middle])

    head.left = sortedListToBST(aList, i, middle-1)
    head.right = sortedListToBST(aList, middle+1, j)

    return head