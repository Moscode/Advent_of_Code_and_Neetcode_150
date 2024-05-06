from collections import deque
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = left

a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def maxRootToLeafPathSum(root):
    totalSum = 0
    if not root:
        return float("-inf")
    
    leftVal = maxRootToLeafPathSum(root.left)
    rightVal = maxRootToLeafPathSum(root.right)
    if leftVal == float("-inf") and rightVal == float("-inf"):
        leftVal, rightVal = 0, 0
    totalSum += max(leftVal + root.val, rightVal + root.val)

    return totalSum

print(maxRootToLeafPathSum(a))
