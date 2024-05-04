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
def breadthFirstValues(root):
    result = []
    stack = deque()
    stack.append(root)
    while stack:
        current = stack.popleft()
        result.append(current.val)
        rightVal = current.right
        leftVal = current.left
        if leftVal:
            stack.append(leftVal)
        if rightVal:
            stack.append(rightVal)

    return result

print(breadthFirstValues(a))


#Recursive Solution
#Since it uses queue not stack the implementation is not direct



    