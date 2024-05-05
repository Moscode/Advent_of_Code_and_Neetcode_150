from collections import deque
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = left

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(2)
e = Node(5)
f = Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#DFS recursively
def treeMinValue(root):
    currentMin = float('inf')
    if not root:
        return float('inf')
    leftVals = treeMinValue(root.left) 
    rightVals = treeMinValue(root.right)
    currentMin = min(leftVals, rightVals, root.val)

    return currentMin

print(treeMinValue(a))

#BFS iteratively
def treeMinValueBF(root):
    currentMin = float("inf")
    if not root:
        return currentMin
    
    queue = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        currentMin = min(current.val, currentMin)
        if (current.left):
            queue.append(current.left)
        if (current.right):
            queue.append(current.right)

    return currentMin

print(treeMinValueBF(a))