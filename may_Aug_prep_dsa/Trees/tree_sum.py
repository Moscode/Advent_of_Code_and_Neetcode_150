from collections import deque
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = left

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#Breadth First Sum
def treeSum(root):
    if not root:
        return 0
    queue = deque()
    queue.append(root)
    sum = 0
    while queue:
        current = queue.popleft()
        sum += current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return sum

print(treeSum(a))

#Depth First Sum using recursion
def treeSumDF(root):
    if not root:
        return 0
    leftVal = treeSumDF(root.right)
    rightVal = treeSumDF(root.left)

    return root.val + leftVal + rightVal

print(treeSumDF(a))