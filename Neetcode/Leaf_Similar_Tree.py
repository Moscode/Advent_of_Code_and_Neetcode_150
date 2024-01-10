# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def recursiveFn(root):
            rootLeaf = []
            if(not root):
                return []
            if(not root.left and not root.right):
                rootLeaf.append(root.val)
            else:
                rootLeaf += recursiveFn(root.left)
                rootLeaf += recursiveFn(root.right)
            return rootLeaf
        return recursiveFn(root1) == recursiveFn(root2)
        