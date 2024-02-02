
 
N = 100

class Node:
    def __init__(self, left=None, right=None, val=0):
        self.value = val
        self.left = left
        self.right = right
 

arr = [0] * N

version = [None] * N
 

def build(node, low, high):
    if low == high:
        node.value = arr[low]
        return
    mid = (low+high) // 2
    node.left = Node()
    node.right = Node()
    build(node.left, low, mid)
    build(node.right, mid+1, high)
    node.value = node.left.value + node.right.value
 


def upgrade(prev, cur, low, high, index, value):
    if index > high or index < low or low > high:
        return
 
    if low == high:
        cur.value = value
        return
 
    mid = (low+high) // 2
    if index <= mid:
        cur.right = prev.right
 
        cur.left = Node()
 
        upgrade(prev.left,cur.left, low, mid, index, value)
    else:
        cur.left = prev.left

        cur.right = Node()
 
        upgrade(prev.right, cur.right, mid+1, high, index, value)
 

    cur.value = cur.left.value + cur.right.value
 
def query(node, low, high, left, right):
    if left > high or right < low or low > high:
        return 0
    if left <= low and high <= right:
        return node.value
    mid = (low+high) // 2
    ls = query(node.left, low, mid, left, right)
    rs = query(node.right, mid+1, high, left, right)
    return ls+rs
 
if __name__ == '__main__':
    A = [1,2,3,4,5]
    n = len(A)
 
    for i in range(n):
        arr[i] = A[i]
 
    # creating Version-0
    root = Node()
    build(root, 0, n-1)
 
    # storing root node for version-0
    version[0] = root
 
    # upgrading to version-1
    version[1] = Node()
    upgrade(version[0], version[1], 0, n-1, 4, 1)
 
    # upgrading to version-2
    version[2] = Node()
    upgrade(version[1], version[2], 0, n-1, 2, 5)
 
    # querying in version-0
    print("In version 0 , query(0,3) :",query(version[0], 0, n-1, 0, 3)) 
 
    # querying in version-1
    print("In version 1 , query(0,4) :",query(version[1], 0, n-1, 0, 4)) 
 
    # querying in version-2
    print("In version 2 , query(3,4) :",query(version[2], 0, n-1, 3, 4))