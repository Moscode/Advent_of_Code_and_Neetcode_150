from collections import deque
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = left

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#Iterative Solution
def depthFirstValues(root):
    result = []
    stack = deque()
    stack.append(root)
    while stack:
        current = stack.pop()
        result.append(current.val)
        rightVal = current.right
        leftVal = current.left
        if rightVal:
            stack.append(rightVal)
        if leftVal:
            stack.append(leftVal)
    return result

print(depthFirstValues(a))

#Recursive Solution
def recusiveDFValues(root):
    result = []
    if not root:
        return result
    leftValues = recusiveDFValues(root.left)
    rightValues = recusiveDFValues(root.right)
    result.append(root.val)
    result.extend(leftValues)
    result.extend(rightValues)
    return result

print(recusiveDFValues(a))



    