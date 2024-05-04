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

#Breadth First Search
def treeInclude(root, target):
    queue = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        if current.val == target:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False

print(treeInclude(a, "c"))

#Recursive Depth First Search

def treeIncludeDFS(root, target):
    if root == None:
        return False
    if root.val == target:
        return True
    leftVals = treeIncludeDFS(root.left, target)
    rightVals = treeIncludeDFS(root.right, target)
    return leftVals or rightVals


print(treeIncludeDFS(a, "w"))
